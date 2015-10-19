import re, random
from people import Staff, Fellow
from rooms import LivingSpace, Office

__author__ = 'Jubril'


class Building(object):
    def __init__(self):
        self.rooms = {
            'offices': [],
            'livingspaces': []
        }
        self.people = []
        self.available_space = (len(self.rooms['offices']) + len(
            self.rooms['livingspaces'])) * len(self.people)

    def __strip_whitespaces(self, line_to_format):
        match = re.search('(\w+\s[^\s]+)\s{0,}(\w+)\s{0,}(\w?)', line_to_format)
        return match.groups()

    def pre_populate(self):
        offices = ['Kiln', 'Bellows', 'Tongs', 'SledgeHammer', 'Furnace', "Mars", "Mercury", "Venus", "Earth", "Jupiter"]
        for office_name in offices:
            office = Office(office_name)
            self.add_room(office, 'offices')

        living_spaces = ['Carat', 'Anvil', 'Heroku', 'Troupon', 'Hacksaw', "Saturn", "Uranus", "Neptune", "Pluto", "Goose"]
        for living_space_name in living_spaces:
            living_space = LivingSpace(living_space_name)
            self.add_room(living_space, 'livingspaces')

    def add_room(self, room, room_type):
        self.rooms[room_type].append(room)

    def read_file(self, input_file):
        with open(input_file, 'r') as f:
            data = f.readlines()
            person = None
            for line in data:
                fullname, role, choice = self.__strip_whitespaces(line)
                # print role
                if role == "STAFF":
                    person = Staff(fullname)
                elif role == "FELLOW":
                    person = Fellow(fullname)
                    if choice == 'Y':
                        person.wants_accomodation()
                self.people.append(person)

    def allocate(self):
        for person in self.people:
            if isinstance(person, Staff):
                room = random.choice(self.rooms['offices'])
                counter = 0
                while not room.is_room_filled() or counter < 100:
                    room = random.choice(self.rooms['offices'])
                    counter += 1
                    break
                print room
                print len(room.occupants)
                if room.is_room_filled():
                    print person
                    room.occupants.append(person)
                    person.allocated = True
                    # break
            elif isinstance(person, Fellow):
                # while len(room.occupants) < Office.max_occupants
                room = random.choice(self.rooms['offices'])
                counter = 0
                while not room.is_room_filled() or counter < 100:

                    room = random.choice(self.rooms['offices'])
                    break
                print room
                print len(room.occupants)
                if room.is_room_filled():
                    print person
                    room.occupants.append(person)
                    person.allocated = True

                if person.choice:
                    print person
                    # assign to living space
                    living_room = random.choice(self.rooms['livingspaces'])
                    print living_room
                    if living_room.is_room_filled():
                        living_room.occupants.append(person)

    def get_allocation_details(self):
        building_offices = self.rooms['offices']
        # print room
        print "The office allocation details shown below"
        for building_office in building_offices:
            print building_office, "\n", building_office.occupants
            # print (key + " (OFFICE)\n", value)

    def get_living_space_details(self):
        living_spaces = self.rooms['livingspaces']
        print "The living space allocatio shown below"
        for living_space in living_spaces:
            print living_space, "\n", living_space.occupants

    def get_members_for_a_particular_office(self, office_name):
        for office in self.rooms['offices']:
            if office_name == office.name:
                return office.get_member_details()
            else:
                return "Office name is not valid"

    def get_a_list_of_unallocated_people(self):
        unallocated_list = []
        for person in self.people:
            if not person.is_allocated():
                unallocated_list.append(person)
        return unallocated_list

if __name__ == '__main__':
    amity = Building()
    amity.pre_populate()
    amity.read_file("input.txt")
    amity.allocate()
    amity.get_allocation_details()
    amity.get_living_space_details()

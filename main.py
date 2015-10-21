import re, random
from models.people import Staff, Fellow
from models.rooms import LivingSpace, Office

__author__ = 'Jubril'


class Building(object):
    def __init__(self):
        self.rooms = {
            'offices': [],
            'livingspaces': []
        }
        self.people = []

    def __strip_whitespaces(self, line_to_format):
        match = re.search('(\w+\s[^\s]+)\s{0,}(\w+)\s{0,}(\w?)', line_to_format)
        return match.groups()

    # prepopulate the offices and living spaces
    def pre_populate(self):
        offices = ['Kiln', 'Bellows', 'Tongs', 'SledgeHammer', 'Furnace', "Mars", "Mercury", "Venus", "Earth", "Jupiter"]
        for office_name in offices:
            self.add_room(Office(office_name), 'offices')

        living_spaces = ['Carat', 'Anvil', 'Heroku', 'Troupon', 'Hacksaw', "Saturn", "Uranus", "Neptune", "Pluto", "Goose"]
        for living_space_name in living_spaces:
            self.add_room(LivingSpace(living_space_name), 'livingspaces')

    def add_room(self, room, room_type):
        self.rooms[room_type].append(room)

    def read_file(self, input_file):
        with open(input_file, 'r') as f:
            data = f.readlines()
            person = None
            for line in data:
                fullname, role, choice = self.__strip_whitespaces(line)

                if role == "STAFF":
                    person = Staff(fullname)
                elif role == "FELLOW":
                    person = Fellow(fullname)
                    if choice == 'Y':
                        person.wants_accomodation()
                self.people.append(person)

    def allocate(self):
        """
        This method allocates fellows and staffs to living rooms
        :return:
        """
        # print random.shuffle(self.rooms['offices'])
        # print random.shuffle(self.rooms['livingspaces'])
        for person in self.people:
            for office in self.rooms['offices']:
                if office.is_room_filled():
                    office.occupants.append(person)
                    break
            # Refactor to shuffle the list and then sequentially pick one at a time
            
            if isinstance(person, Fellow) and person.choice:
                    # print person
                    # assign to living space
                    living_room = random.choice(self.rooms['livingspaces'])
                    # print living_room
                    if living_room.is_room_filled():
                        living_room.occupants.append(person)

    def get_allocation_details(self):
        building_offices = self.rooms['offices']
        print "The office allocation details shown below"
        for building_office in building_offices:
            print building_office, "(OFFICE)", "\n", building_office.occupants

    def get_living_space_details(self):
        living_spaces = self.rooms['livingspaces']
        print "The living space allocatio shown below"
        for living_space in living_spaces:
            print living_space, "(LIVING)", "\n", living_space.occupants

    def get_members_for_a_particular_office(self, office_name):
        for office in self.rooms['offices']:
            if office_name == office.name:
                return office.get_member_details()
            else:
                return "Office name is not valid"

    def get_a_list_of_unallocated_people(self):
        """
            This method gets a list of unallocated people
        """
        unallocated_list = []
        for person in self.people:
            if not person.is_allocated():
                unallocated_list.append(person)
        return unallocated_list

if __name__ == '__main__':
    amity = Building()
    amity.pre_populate()
    amity.read_file("data/input.txt")
    amity.allocate()
    amity.get_allocation_details()
    amity.get_living_space_details()
    amity.get_members_for_a_particular_office("Kiln")

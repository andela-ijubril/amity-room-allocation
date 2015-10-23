import re, random
from models.people import Staff, Fellow, Person
from models.rooms import LivingSpace, Office

__author__ = 'Jubril'


class Building(object):
    def __init__(self):
        self.rooms = {
            'offices': [],
            'livingspaces': []
        }
        self.people = []
        self.allocated_offices = []
        self.allocated_rooms = []
        self.unallocated_list = []

    def __strip_whitespaces(self, line_to_format):
        """
        This method strip the text input in the format
        ANDREW PHILLIPS	FELLOW	Y to the following 3 groups which represents the name, role and choice
        :param line_to_format:
        :return: the groups
        """
        match = re.search('(\w+\s[^\s]+)\s{0,}(\w+)\s{0,}(\w?)', line_to_format)
        return match.groups()

    def pre_populate(self):
        """
        This method prepopulates the office and LivingSpace object with 10 offices and living spaces
        """
        offices = ['Kiln', 'Bellows', 'Tongs', 'SledgeHammer', 'SledgeHammer', 'Furnace', "Mars", "Mercury", "Venus", "Earth"]
        for office_name in offices:
            self.add_room(Office(office_name), 'offices')

        living_spaces = ['Carat', 'Anvil', 'Heroku', 'Troupon', 'Hacksaw', "Saturn", "Uranus", "Neptune", "Pluto", "Goose"]
        for living_space_name in living_spaces:
            self.add_room(LivingSpace(living_space_name), 'livingspaces')

    def add_room(self, room, room_type):
        """
        This method add an office or living space depending on the room type passed as a parameter
        :param room:
        :param room_type:
        """
        self.rooms[room_type].append(room)

    def add_person(self, name, role):
        """
        This method adds a person to staff or fellow class depending on the role
        :param name:
        :param role:
        """
        try:
            if role == "STAFF":
                self.people = Staff(name)
            elif role == "FELLOW":
                self.people = Fellow(name)
        except ValueError:
            return "Invalid role name"

    def read_file(self, input_file):
        """
        This method  read file from an input file give as a parameter
        :param input_file:
        """
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
        This method allocates fellows and staffs to offices
        It also allocate fellows who are interested in getting a room living space
        """
        random.shuffle(self.rooms['offices'])
        random.shuffle(self.rooms['livingspaces'])
        for person in self.people:
            for office in self.rooms['offices']:
                if office.is_room_filled():
                    self.rooms['offices'].remove(office)
                    continue
                office.occupants.append(person)
                if office not in self.allocated_offices:
                    self.allocated_offices.append(office)
                person.office = office
                break

            if isinstance(person, Fellow) and person.choice:
                for living_room in self.rooms['livingspaces']:
                    if living_room.is_room_filled():
                        self.rooms['livingspaces'].remove(living_room)
                        continue
                    living_room.occupants.append(person)
                    if living_room not in self.allocated_rooms:
                        self.allocated_rooms.append(living_room)
                    person.living = living_room
                    break

    def get_allocation_details(self):
        """
            This method gets the details of those allocated to offices
        """
        building_offices = self.allocated_offices
        print "The office allocation details shown below"
        for building_office in building_offices:
            print building_office, "(OFFICE)", "\n", building_office.occupants

    def get_living_space_details(self):
        """
            This method gets the details of those allocated to Living Spaces
        """
        living_spaces = self.allocated_rooms
        print "The living space allocation shown below"
        for living_space in living_spaces:
            print living_space, "(LIVING)", "\n", living_space.occupants

    def get_person_details(self, full_name):
        """
        Get the office a person is allocated to
        :param full_name:
        """
        person = Person(full_name)
        if person in self.people:
            person_index = self.people.index(person)
            person = self.people[person_index]
            if person.get_office():
                return person.get_office().occupants
        else:
            return "Not a valid name"

    def remove_from_room(self, name):
        """
        This method removes an employee from an office space
        :param name:
        """
        person = Person(name)
        if person in self.people:
            person_index = self.people.index(person)
            person = self.people[person_index]
            if person.get_office():
                return person.get_office().occupants.remove(person)
        else:
            return "Name not valid"

    def get_members_for_a_particular_office(self, office_name):
        """
        This method returns the members in a particular office that is passed in the parameters
        :param office_name:
        :return: Member details in the office
        """
        for office in self.allocated_offices:
            if office_name == office.name:
                return office.get_member_details()

    def get_a_list_of_unallocated_people(self):
        """
            This method gets a list of unallocated people
            :return: List of unallocated people
        """

        for person in self.people:
            if not person.is_allocated():
                self.unallocated_list.append(person)
        return self.unallocated_list

if __name__ == '__main__':
    amity = Building()
    amity.pre_populate()
    amity.read_file("data/input.txt")
    amity.allocate()
    amity.get_allocation_details()
    amity.get_living_space_details()

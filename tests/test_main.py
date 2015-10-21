import unittest
from main import Building
import __builtin__ as builtin
from models.rooms import Office
from models.people import Person, Fellow, Staff

__author__ = 'Jubril'


class TestingOfficeAllocation(unittest.TestCase):

    def setUp(self):
        self.amity = Building()
        # self.room = Office("Kiln")
        # self.person = Person("Jubril")

    def test_can_add_office(self):
        self.amity.add_room("Codango", 'offices')
        self.assertIn('Codango', self.amity.rooms['offices'])

    def test_can_add_livingspace(self):
        self.amity.add_room("Troupon", 'livingspaces')
        self.assertIn('Troupon', self.amity.rooms['livingspaces'])

    def test_can_prepopulate(self):
        self.amity.pre_populate()
        self.assertEquals('Kiln', self.amity.rooms['offices'][0].name)
        self.assertEquals(len(self.amity.rooms['offices']), 10)
        # self.assertIsInstance('Kiln', Office)
        # self.assertIn('Kiln', self.amity.rooms['offices'])

    def test_file_was_read(self):
        # self.amity.read_file("input.txt")
        self.assertIsNone(self.amity.read_file("data/input.txt"))

    def test_list_of_unallocated_people(self):
        self.assertIsNotNone(self.amity.get_a_list_of_unallocated_people())

    def test_get_allocation_details(self):
        self.assertIsNone(self.amity.get_allocation_details())
        self.assertIsNone(self.amity.get_living_space_details())

    def test_get_members_for_aparticular_office(self):

        self.assertIsNone(self.amity.get_members_for_a_particular_office("Kiln"))

    def test_allocate(self):
        self.amity.pre_populate()
        self.amity.read_file("data/input.txt")
        self.assertIsNone(self.amity.allocate())


if __name__ == '__main__':
    unittest.main()

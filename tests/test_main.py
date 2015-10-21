import unittest
from main import Building
import __builtin__ as builtin
from models.rooms import Office
from models.people import Person, Fellow, Staff

__author__ = 'Jubril'


class TestingOfficeAllocation(unittest.TestCase):

    def setUp(self):
        self.amity = Building()
        self.fellow = Fellow("jubril")

    def test_can_add_office(self):
        """
        Test if an office can be added
        """
        self.amity.add_room("Codango", 'offices')
        self.assertIn('Codango', self.amity.rooms['offices'])

    def test_can_add_livingspace(self):
        """
        Test if a living space can be added
        """
        self.amity.add_room("Troupon", 'livingspaces')
        self.assertIn('Troupon', self.amity.rooms['livingspaces'])

    def test_can_prepopulate(self):
        """
        Test if offices and living space can be prepopulated
        """
        self.amity.pre_populate()
        self.assertEquals('Kiln', self.amity.rooms['offices'][0].name)
        self.assertEquals(len(self.amity.rooms['offices']), 10)
        self.assertEquals('Carat', self.amity.rooms['livingspaces'][0].name)
        self.assertEquals(len(self.amity.rooms['livingspaces']), 10)

    def test_file_was_read(self):
        """
        Test to see if the file was read
        """
        self.assertIsNone(self.amity.read_file("data/input.txt"))

    def test_list_of_unallocated_people(self):
        """
        Test to see get list of unallocated people
        """
        self.assertIsNotNone(self.amity.get_a_list_of_unallocated_people())

    def test_get_allocation_details(self):
        """
        Test to get the list of office allocations
        """
        self.assertIsNone(self.amity.get_allocation_details())
        self.assertIsNone(self.amity.get_living_space_details())

    def test_get_members_for_a_particular_office(self):
        """
        Test to get the members of a particular office
        """
        self.assertIsNone(self.amity.get_members_for_a_particular_office("Kiln"))

    def test_allocate(self):
        self.amity.pre_populate()
        self.amity.read_file("data/input.txt")
        self.assertIsNone(self.amity.allocate())


if __name__ == '__main__':
    unittest.main()

import unittest
from models.people import Person, Fellow, Staff
__author__ = 'masterp'


class TestingPeople(unittest.TestCase):

    def setUp(self):
        self.fellow = Fellow("Ini")
        self.staff = Staff("Chidi")

    def test_wants_accomodation(self):
        """
        Test if the method returns
        """
        self.assertIsNone(self.fellow.wants_accomodation(True))

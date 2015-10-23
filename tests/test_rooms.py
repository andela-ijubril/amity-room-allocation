import unittest
from models.rooms import Office, LivingSpace, Room
__author__ = 'masterp'


class TestingRooms(unittest.TestCase):

    def setUp(self):
        self.office = Office("Mercury")
        self.living_space = LivingSpace("Jupiter")

    def test_has_no_occupant(self):
        """
        This method test if the room or offices has no occupant
        """
        self.assertFalse(self.office.has_no_occupant())
        self.assertFalse(self.living_space.has_no_occupant())

    def test_get_member_details(self):
        """
        This method test the get member details
        """
        self.assertIsNotNone(self.office.get_member_details())
        self.assertIsNotNone(self.living_space.get_member_details())

    def test_is_room_filled(self):
        """
        This method test if the room is filled
        """
        self.assertFalse(self.office.is_room_filled())
        self.assertFalse(self.living_space.is_room_filled())

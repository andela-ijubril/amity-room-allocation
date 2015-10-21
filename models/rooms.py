import abc

__author__ = 'Jubril'


class Room(object):
    __metaclass__ = abc.ABCMeta

    max_occupants = 4

    def __init__(self, name):
        self.name = name
        self.occupants = []

    def get_member_details(self):
        """
        Get the details of the occupants in a room
        :return: occupants
        """
        return self.occupants

    def is_room_filled(self):
        """
            This method checks if the room is filled
        :return: Boolean
        """
        if len(self.occupants) < self.max_occupants:
            return True
        else:
            return False

    def has_no_occupant(self):
        """
        This method checks if the current room has any occupants
        :return: Boolean
        """
        if len(self.occupants) > 0:
            return True
        else:
            return False


class LivingSpace(Room):
    def __repr__(self):
        return self.name


class Office(Room):
    max_occupants = 6

    def __repr__(self):
        return self.name

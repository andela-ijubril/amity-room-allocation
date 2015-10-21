import abc

__author__ = 'Jubril'


class Room(object):
    __metaclass__ = abc.ABCMeta

    max_occupants = 4

    def __init__(self, name):
        self.name = name
        self.occupants = []

    # Get the occupants in the room
    def get_member_details(self):
        return self.occupants

    # check if the current room is filled
    def is_room_filled(self):
        if len(self.occupants) < self.max_occupants:
            return True
        else:
            return False

    # check if the current room has any occupants
    def has_no_occupant(self):
        if len(self.occupants) > 0:
            return True
        else:
            return False

    def is_female(self):
        pass


class LivingSpace(Room):
    def __repr__(self):
        return self.name


class Office(Room):
    max_occupants = 6

    def __repr__(self):
        return self.name

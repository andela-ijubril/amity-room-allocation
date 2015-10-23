import abc
__author__ = 'Jubril'


class Person(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name):
        self.name = name
        self.allocated = False
        self.office = None

    def __eq__(self, obj):
        return self.name == obj.name

    def is_allocated(self):
        """
        This method checks if the current person is allocated
        """
        return self.allocated

    def get_office(self):
        """
        Get the current office of the person
        :return:
        """
        return self.office


class Staff(Person):
    def __repr__(self):
        return self.name


class Fellow(Person):
    def __init__(self, name):
        super(Fellow, self).__init__(name)
        self.choice = False
        self.living = None

    def __repr__(self):
        return self.name

    def wants_accomodation(self, choice=True):
        """
        This methods checks if the Fellow wants an accommodation
        :param choice:
        """
        self.choice = choice

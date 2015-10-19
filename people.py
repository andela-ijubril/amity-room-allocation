import abc
__author__ = 'Jubril'


class Person(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name):
        self.name = name
        self.allocated = False

    def is_allocated(self):
        return self.allocated


class Staff(Person):
    def __repr__(self):
        return self.name


class Fellow(Person):
    def __init__(self, name):
        super(Fellow, self).__init__(name)
        self.choice = False

    def __repr__(self):
        return self.name

    def wants_accomodation(self, choice=True):
        self.choice = choice

"""
Module for the Base class.
"""

class Base:
    """
    A class representing the base class for other classes in the project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the Base class.

        :param id: The id of the instance (default is None).
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
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

    @staticmethod
    def integer_validator(name, value):
        """
        Validates the value to be an integer greater than 0.

        :param name: The name of the value.
        :param value: The value to be validated.
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is less or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
"""writing a fonction  for the task Exact same object """
class BaseGeometry:
    """
    A class representing the base geometry.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
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

    def __dir__(self):
        """
        Returns the attributes of the object.

        :return: List of attributes.
        :rtype: list
        """
        return [
            '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
            '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
            '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
            '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
            '__subclasshook__', '__weakref__', 'area', 'integer_validator'
        ]

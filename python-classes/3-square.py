""" writing a class for the task  Access and update private attribute  """
class Square:
    """
    This class defines a square by its size.
    """

    def __init__(self, size=0):
        """
        Initializes a square with an optional size.

        :param size: The size of the square (default is 0).
                     Must be an integer, otherwise raise a TypeError exception.
                     If size is less than 0, raise a ValueError exception.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        :return: The size of the square.
        :rtype: int
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        :param value: The new size for the square.
                      Must be an integer, otherwise raise a TypeError exception.
                      If value is less than 0, raise a ValueError exception.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        :return: The area of the square.
        :rtype: int
        """
        return self.__size * self.__size
    
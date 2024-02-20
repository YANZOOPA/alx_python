""" writing a class for the task Size validation """
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        :return: The area of the square.
        :rtype: int
        """
        return self.__size * self.__size

    def get_size(self):
        """
        Gets the size of the square.

        :return: The size of the square.
        :rtype: int
        """
        return self.__size

    def set_size(self, new_size):
        """
        Sets the size of the square.

        :param new_size: The new size for the square.
                         Must be an integer, otherwise raise a TypeError exception.
                         If new_size is less than 0, raise a ValueError exception.
        """
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")

        if new_size < 0:
            raise ValueError("size must be >= 0")

        self.__size = new_size

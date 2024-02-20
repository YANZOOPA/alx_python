"""writing a class that generate a  Square with size """
class Square:
    """
    This class defines a square by its size.
    """

    def __init__(self, size):
        """
        Initializes a square with the given size.

        :param size: The size of the square.
        """
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        :return: The area of the square.
        """
        return self.__size * self.__size

    def get_size(self):
        """
        Gets the size of the square.

        :return: The size of the square.
        """
        return self.__size

    def set_size(self, new_size):
        """
        Sets the size of the square.

        :param new_size: The new size for the square.
        """
        self.__size = new_size

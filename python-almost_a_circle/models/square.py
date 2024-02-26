"""
Module for the Rectangle class.
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    A class representing a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the Square class.

        :param size: The size of the square (width and height).
        :param x: The x-coordinate of the square (default is 0).
        :param y: The y-coordinate of the square (default is 0).
        :param id: The id of the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

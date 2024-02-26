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

    def __str__(self):
        """
        Return a string representation of the Square.

        :return: String representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

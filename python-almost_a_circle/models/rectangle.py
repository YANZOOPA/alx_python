"""
Module for the Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
    A class representing a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the Rectangle class.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param x: The x-coordinate of the rectangle (default is 0).
        :param y: The y-coordinate of the rectangle (default is 0).
        :param id: The id of the rectangle (default is None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        self.integer_validator("width", value)
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        self.integer_validator("height", value)
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        self.integer_validator("x", value)
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        self.integer_validator("y", value)
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the Rectangle.

        :return: The area of the Rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Print the Rectangle instance with the character #.

        """
        for _ in range(self.__height):
            print("#" * self.__width)

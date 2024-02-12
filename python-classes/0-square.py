#python3 -c 'print(__import__("my_module").__doc__)'
class Square:
    #python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        #python3 -c 'print(__import__("my_module").my_function.__doc__)'
        #python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

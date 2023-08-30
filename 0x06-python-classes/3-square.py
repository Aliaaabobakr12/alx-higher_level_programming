#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size = 0):
        """
        Initializes a new Square instance.
        and size of the square.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    """Return the area of the square"""

    def area(self):
        return (self.__size) * (self.__size)

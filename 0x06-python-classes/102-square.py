#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (float or int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size  # Using the size setter

    @property
    def size(self):
        """
        Getter method for the size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (float or int): The new size value.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparison operator.

        Args:
            other (Square): The other Square to compare.

        Returns:
            bool: True if both squares have the same area, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparison operator.

        Args:
            other (Square): The other Square to compare.

        Returns:
            bool: True if the squares have different areas, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less than comparison operator.

        Args:
            other (Square): The other Square to compare.

        Returns:
            bool: True if the area of self is less than the area of other, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal to comparison operator.

        Args:
            other (Square): The other Square to compare.

        Returns:
            bool: True if the area of self is less than or equal to the area of other, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater than comparison operator.

        Args:
            other (Square): The other Square to compare.

        Returns:
            bool: True if the area of self is greater than the area of other, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal to comparison operator.

        Args:
            other (Square): The other Square to compare.

        Returns:
            bool: True if the area of self is greater than or equal to the area of other, False otherwise.
        """
        return self.area() >= other.area()


if __name__ == "__main__":
    # Test the implementation with the provided example
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")

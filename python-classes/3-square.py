#!/usr/bin/python3
"""
Area of a square
Write a class Square that defines a square by: (based on 2-square.py)
"""


class Square:

    """
    Square class with a private instance attribute size.
    """

    def __init__(self, size=0):
        """Define Private instance attribute: size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return self.__size ** 2

#!/usr/bin/python3
"""
Access and update private attribute
Write a class Square that defines a square by: (based on 3-square.py)
"""


class Square:
    """
    Square class with a private instance attribute size.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size ** 2

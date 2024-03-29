#!/usr/bin/python3
"""
Printing a square
Write a class Square that defines a square by: (based on 4-square.py)
"""


class Square:
    """
    Square class with private instance attribute size.
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

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

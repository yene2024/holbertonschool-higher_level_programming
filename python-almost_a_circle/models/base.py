#!/usr/bin/python3
"""1. Base class """


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        """
        a function that assign the public
        instance attribute id with this argument
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

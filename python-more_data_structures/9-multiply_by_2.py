#!usr/bin/python3
def multiply_by_2(a_dictionary):
    new_directory = {}
    for key, value in a_dictionary.items():
        new_directory = value * 2
    return new_directory

#!usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = dict(a_dictionary)
    for key in new_dictionary:
        new_dictionary *= 2
    return new_dictionary

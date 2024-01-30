#!usr/bin/python3
def multiply_by_2(a_dictionary):
    multiplied_items = ((k, v * 2) for k, v in a_dictionary.items())
    return dict(multiplied_items)

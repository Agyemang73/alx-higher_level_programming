#!/usr/bin/python3
def print_sorted_dictionar(a_dictionary):
    keys = sorted(list(a_dictionary.keys()))
    for item in keys:
        print("{0}: {1}".format(item, a dictionary.get(item)))

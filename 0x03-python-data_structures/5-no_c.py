#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for x in my_string:
        if x is not 'c' and x is not 'C':
            new += x
    return new

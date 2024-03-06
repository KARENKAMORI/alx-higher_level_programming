#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    x = 0

    if type(roman_string) is str and roman_string:
        for char in range(len(roman_string) - 1, -1, -1):
            if roman_value[roman_string[char]] >= x:
                result += roman_value[roman_string[char]]
            else:
                result -= roman_value[roman_string[char]]
            x = roman_value[roman_string[char]]
    return result

#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    skipno = 0
    if type(roman_string) != str and roman_string is None:
        return 0
    for m, lett in enumerate(roman_string):
        if skipno == 0:
            if lett in rom:
                if m < (len(roman_string) - 1):
                    if rom[lett] < rom[roman_string[m + 1]]:
                        number += (rom[roman_string[m + 1]] - rom[lett])
                        skipno = 1
                        continue
                    else:
                        number += rom[lett]
                else:
                    return 0
        skipno = 0
    return number

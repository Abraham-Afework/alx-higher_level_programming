#!/usr/bin/python3
def roman_to_int(roman_string):

    roman_No = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'XL': 40, 'CD': 400}
    roman_No_2 = {'X': 10, 'L': 50, 'XC': 90, 'C': 100, 'D': 500, 'M': 100}
    roman_No.update(roman_No_2)
    sum = 0
    i = 0
    if roman_string is None or type(roman_string) != str:
        return 0
    else:
        while i < len(roman_string):

            current_char = roman_string[i:i+2]

            if current_char in roman_No:
                sum += roman_No[current_char]
                i += 2
            else:
                sum += roman_No[roman_string[i]]
                i += 1
        return sum

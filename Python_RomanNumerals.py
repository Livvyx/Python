"""
Olivia Walker
CS202
Exercise 4.

Description:
Write a program that prompts the user to enter a number within the range of 1 through 10.
the program should display the roman numeral version of that number.
if the number is outside the range of 1 through 10, the program should display
and error message. the following table shows the roman numerals for the numbers 1 through 10:
(example on pdf)
"""

# Displaying Roman Numerals

number = int(input("* Please enter a number from 1 - 10 to see the roman numeral: "))  # Input for user to enter 1 - 10

print("The Number You Entered & Converted To Roman Numeral is: ")  # output

RomanNumerals = ["NULL", "I", "II", "III", "IV", "V", "VI", "VII", "IX", "X"]  # Constructor?


print(RomanNumerals[number])  # Get the index and display the string

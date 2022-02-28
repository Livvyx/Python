"""
Olivia Walker
CS202
Exercise 3

Description:
Write a program that asks the user to enter a persons age.
the program should display a mesage indicating wether the persons
an infant, a child, a teenager, or an adult.
Following the guidlines:

* If the person is 1 year old or less, he or she is an infant.
* If the person is older then 1 year, but younger than 13 years, he or she is a child.
* If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
* If the person is at least 20 years old, he or she is an adult.
"""

Age = int(input("* Kia Ora Please Input Your Age: "))  # input for the user to enter their age

if Age > 13:  # if statement for when the user inputs a number that is more then 13 and less then 18

    print("***Your A Teenager!***")  # output if the user enter more then 13

elif Age > 18:  # else if statement for when the user inputs more then 18

    print("***Your A Adult!***")  # output if the user enters more then 18

else:  # else statement for when the user enters less then 13

    print("***Your A infant!***")  # output if the user enters less then 13


"""
Olivia Walker
CS202
Exercise 5

Description:
Scientists measure an object's mass in kilograms and its weight in newtons.
If you know the amount of mass of an object in kilograms, you can calculate its weight
in newtons with the following formula:

weight = mass x 9.8

write a program that asks the user to enter an object's mass, then calculate its weight. if
the object weighs more than 500 newtons, display a message indicating that it is too heavy.
if the object weighs less than 100 newtons, display a message indicating that is is too light.
"""


''' * Scientist measure an objects mass in kgs and weight in newtons with the following formula weight = mass x 9.8 '''

weight = float(input("Enter The Weight In Kgs: "))  # Take user input

newtons = weight * 9.8  # weight times 9.8

print(newtons)  # printing the newtons output for weight times 9.8

if newtons < 100:  # if statement for newtons weight times 9.8 and if less then 100
    print("The Weight is too light")  # output if less than 100
elif newtons > 500:  # if statement for newtons weight times 9.8 and more than 500
    print("The Weight is too heavy")  # output if more than 500




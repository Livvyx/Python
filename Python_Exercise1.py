"""
* Olivia Walker
* CS202 Python
* Chapter 5, Exercise 1
Kilometer Converter:
Write a program that asks the user to enter a distance in kilometers,
then convert that distance to miles. the conversion formula is as follows:
Miles = Kilometers X 0.6214
"""
# output
print('\n * * * * * Kilometer Converter * * * * * ')
# taking kilometers input from user
Km = float(input("\nKia Ora Please Enter A Value In Kilometers: "))
# Calculating
Miles = Km * 0.6214
# Outputting
print("Awesome The %0.2f Kilometers is calculated into %0.2f Miles! " %(Km, Miles))
# The %0.2f simplifies it down to only 2 decimals


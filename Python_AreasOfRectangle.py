"""
Olivia Walker
CS202
Programming Exercise 2
Area's Of A Rectangle

Description:
The Area of a rectangle is the rectangles length times its width.
Write a program that asks for the length and width of two rectangles.
The program should tell the user which rectangle has the greater area,
or if the areas are the same.

Formula = a(Area) = l(Length) * w(Width)
"""

 # finding the Area of a Rectangle

width = float(input('Please enter width of a rectangle: '))  # having the user input the width
length = float(input('Please enter length of a rectangle: '))  # having the user input the height

# calculating the area by multiplying width by height
Area = width * length

print("\nArea of a Rectangle is: %.2f" %Area)  # outputting the calculation of width x height from the area


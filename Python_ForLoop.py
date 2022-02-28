"""
Olivia Walker
CS202 Python
For Loop
"""

myList = [2, 4, 7, 8, 9, 6, 5, 4, 3]  # defining a list

print("index 5" + str(myList[5]))

    # Nested for loop to loop through a list
for x in myList:  # creating a for loop

    if (x > 4):  # creating a if statement if x is more then the integer 4, output it

        print(x)  # if no curly brackets needs indents

    # For loop to iterate 10 times

    loopTimes = 10
    # for loop above has ended here because of indentation
for x in range(loopTimes):
    print("iteration number" + str(x+1))
    y = x * 10
    print(y)
    for z in range(10):  # nested for loop
        print(z)
        print("nested for loop")
print("For Loop Has Ended!")
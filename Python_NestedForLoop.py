"""
Olivia Walker
CS202 Python
Lists 2
"""
  # change the name of this to nested for loop in files
myList = [2, 4, 7, 8, 9, 6, 5, 4, 3]  # defining a list

print("index 5" + str(myList[5]))

    # Nested for loop to loop through a list
for x in myList:  # creating a for loop

    if (x > 4):  # creating a if statement if x is more then the integer 4, output it

        print(x)  # if no curly brackets needs indents

    # For loop to iterate 10 times
    loopTimes = 10
    for z in range(loopTimes):
        print("iteration number" + str(z+1))
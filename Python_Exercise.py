"""
Python Exercise
CS203
Olivia Walker
Exercise: Distance Travelled
- Enter the time a car was travelling.

1. find the distance travelled in 3 different scenarios.
50km/hr
100km/hr
120km/hr

Hint: distance = Speed X Time
"""

print("Enter the time of your car travelling")
print("* * * * * * * * * * * * * * * * * * *")

time = input("Enter Your Time:")  # assigning a variable to time input
time = int(time)  # assigning time to integer
# print(time)  # outputting time
speed1 = 50
speed2 = 100
speed3 = 120
distance1 = time * speed1
distance2 = time * speed2
distance3 = time * speed3

print("Distance Travelled Via 50km:" + str(distance1))
print("Distance travelled via 100km:" + str(distance2))
print("Distance travelled via 120:" + str(distance3))





















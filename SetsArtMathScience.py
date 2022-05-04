"""
CS203
Python
"""

# Creating a set
art = {"Olivia", "Sam", "Peter", "Louise"}
science = {"Jason", "Luke", "Sarah", "Will"}
math = {"Simon", "Larissa", "Keith", "Rob"}

# Ouputting
print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print("The current students enrolled in Maths & Science are: ", math.intersection(science))
print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print("The Current Students Enrolled in Science are: ", science.difference(art.union(math)))
print("\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print("The Current Students Enrolled in Art are: ", art.difference(math.union(science)))
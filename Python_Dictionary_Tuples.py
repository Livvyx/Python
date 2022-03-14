"""
* Olivia Walker
* CS202 Python
Dictionary & Sets
"""

print("\n* * * My Tuples * * *")
# Creating a tuple
OliviaTuple = ("\nWho", "What", "Where", "When")
# outputting
print(OliviaTuple)
# printing the length
print(len(OliviaTuple))

print("\n* * *Printing my dictionary * * *")

MyDictionary = {"epmid": 658, "name": "Olivia", "department": "Sales"}
print(MyDictionary)

print("\n* * * Alocating Last Name For Olivia * * *")
MyDictionary["last name"] = "Walker"
print(("The Last Name: ") + MyDictionary["last name"])
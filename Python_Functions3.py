"""
Olivia Walker
CS202 Python
Functions - return values
"""
def DisplayAge(name, age = 1):
    print( name + ' is ' + str(age) + ' Years Old And Legally Of Age')  # output the
def IsAdult(age):
    if(age>18):
        return True  # return if age is over 18
    else:
        return False  # return if age is under 18
CharacterAge=20
DisplayAge("Olivia", CharacterAge)
print(IsAdult(19))

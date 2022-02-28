"""
Olivia Walker
CS202
Programming Exercise 6

Description:
The Date June 10, 1960, is special because when it is written in the following format,
the month times the day equals the year 6/10/60. (year = month * day = 6/10/60)

Design a program that asks the user to enter a month(in numeric form), a day, and a two-digit year.
the program should then determine whether the month times the day equals the year. (month*day=year).
if so, it should display a message saying the date is magic. otherwise, it should display a message,
saying the date is not magic.
"""
#Magic Dates
print("\t\n***** Kia Ora Please Enter A Date In Numeric form dd/mm/yyyy*****")  # outputting to guide the user
day = int(input("\t\n* Enter a day 1 - 31: "))  # input for user to enter day between 1 and 31
month = int(input("\t\n* Enter month 1- 12: "))  # input for user to enter year between 1 and 12
year = int(input("\t\n* Enter A Numeric Year eg (1960 = 60 or 2011 = 11): "))  # enter a numeric number for a year

output = format(day)+"/"+format(month)+"/"+format(year)

print(output)
#if day * month does not = year print not

if (day * month) != year:
    print("\t\n* Darn!..This is not a magic number")
else:
    print("\t\n.*+.*+You found a Magic Number!.*+.*+")


"""
Olivia Walker
CS202

"""


EmployeeFile = open('employeeDetails.txt', 'w')
EmployeeFile.write("Samuel\n")
EmployeeFile.write("Alex\n")
EmployeeFile.close()
EmployeeFileOutput = open('employeeDetails.txt', 'r')
print(EmployeeFileOutput.readline())
print(EmployeeFileOutput.readline())
EmployeeFileOutput.close()


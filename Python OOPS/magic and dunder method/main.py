from emp import Employee  #this is imported from the class that is created with the name emp.py

emp = Employee()  
print(str(emp)) #This doesn't print anything so to print the details we need to declare str function in emp.py
print(repr(emp))
# print(emp.name)
# print(len(emp.name))
emp()   
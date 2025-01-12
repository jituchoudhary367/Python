"""
Access modifiers :- 
1.Public
2.Private
3.Protected

"""

#Protected access modifiers = whether there is no concept of public , private and protected access modifiers but can be used.
class Employee:
    def __init__(self):
        self.__name = "Jitendra"  #Here the __ refers to protected access modifier
        
a = Employee()
# print(a.__name) #This will throw an error because it is private variable.This can not be accessed directly.
print(a._Employee__name) #This is called name mangling in python. can be accessed indirectly using name mangling.

print(a.__dir__())
#This will shows all the methods that can be applied on a.

"""Python Boolean type"""
a = True
print(type(a)) #<class 'bool'>
b = False
print(type(b)) #<class 'bool'>


"""Python bool() Function"""
x = None
print(bool(x)) # Returns ""False"" as x is None
x = ()
print(bool(x)) # Returns ""False"" as x is an empty sequence
x = {}
print(bool(x)) # Returns ""False"" as x is an empty dictionary
x = 0.0
print(bool(x)) # Returns ""False"" as x is 0
x = 'Jitendra Chaudhary'
print(bool(x)) # Returns ""True"" as x is a non empty string



"""Integers and floats as Boolean"""
var1 = 0
print(bool(var1))  #False
var2 = 1
print(bool(var2)) #True
var3 = -9.7
print(bool(var3)) #True


a = 0
if not a:
    print("False")
    
a = 2
b = 8
if a == 2:
    print("True") 
if a !=b:
    print("True")
    
    
    
"""Python In operator"""    
a = 5
b = 4
if a is b:
    print("True")
else:
    print("False")  #returns "False" as a and b are not equal.
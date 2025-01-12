"""
a="1"
b="2"
print(The sum is , a+b) ==> 12
#because here  a and b are strings so they are concatenated as a string 
"""

#Typecasting

#Explicit typecasting
a="1"
b="2"
print("The sum is : ", int(a)+int(b))



"""
name1 = "Jitendra"
name2 = "Chaudhary"
print("The sum is : ",int(name1)+int(name2)) #TypeError: can only concatenate str (not "int") to str
#because here name1 and name2 are strings so they are concatenated as a string 
#Returns Error 
"""


"""
There are two types of conversion 
1. Explicit Type conversion
2. Implicit Type conversion

"""

#Implicit typecasting
a = 4849.9393
b = 393993     # here the sum is in float because the implicit typecasting it's done automatically
print("The sum of the number is :",a+b)

print("the type of a is :",type(a))
print("the type of b is :",type(b))
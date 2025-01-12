name = "Jitendra"
friend = "Alexender"

Introduction = "Alexender is from America. \n he is currently living in dubai.\n He is the owner of the luxury car showroom named \"CarExpert\""

BMW = '''
Bawerian motor works is a German based company,
Which is the designer of the luxury cars
The cars are created by the company are full of comforts and luxury
"This is all about the company
'''

print(name)
print(friend)
print(Introduction)

"""
In array string is like an array of character which can be accessed by index 
 Index that is not present if it accessed using any function then it'll show error.  
"""
print(name[0])
print(name[3])

print("Hello , "+name)
print(BMW)

#Using a for loop for printing the characters of the string
for character in BMW:
    print(character)
    
    
"""
Stings
"""  
  
#==>>String      
# s = 'Jitendra chaudhary'
# s1 = "Jitendra chaudhary"

# print(s)
# print(s1)4

#multiline strings
# s = """Hello what are you doing
#     you are on the way to learn the python
#     So let's start with the basics
# """    

# print(s)

#Access the elements
s = "Jitendra Chaudhary"

# print(s[7])  #=>Positive indexing starts from zero 
# print(s[-2])  #=>Negative indexing starts from -1 
# print(s[3:4]) #String slicing start and end index
# print(s[::-1])# Reverse a string
# # s[0] = "H" #not possible to change the string because strings are immutable in python
# print(s)
# s2 = s.replace("Hitendra","Jitu") #M-2 =>String updation
# #instead of that need to create a new string
# s = "H" +s[1:] #M-1 => String updation
# print(s2)
# # del s2
# # print(s2) => it is deleted that is why if we try to print then it will be throwing the error
# print(len(s2))
# print(s.upper())
# print(s.lower())
# s3 = "  Jitu Choudhary    "
# print(s3.strip()) #=>remove the blanks from both the side starting and ending
# print(s3.replace("Jitu","Ram"))
    





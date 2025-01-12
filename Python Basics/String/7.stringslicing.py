name ="Jitendra Chaudhary"

print(name[0:8])
"""
1. to print the sequence of the character from the string just need to specify the number of the 
character that you want to print you just need to mention in the [start : end] with the name of the function/variable[start:end]
2.len() => is used to print the length of the variable.

"""

# This is called string slicing
#For the slicing it will print upto n-1 position (Ex:- 0 to 8 = chars but not print the space)
len1 = len(name)
print("Jitendra is a",len1,"letter word")
print(len1)
print(name[0:8])
print(name[:8])
print(name[:])
print(name[1:])
#this is used to slice the number of chars from the beginning and end
print(name[0:-3])
print(name[0:len(name)-3]) #this is same as the it's previous one
print(name[-3:-7])
print(name[:-8])
print(name[::-1])


"""
Quick Quiz 
Name="Jitendra"
print(name[-4:-5])

Result : empty space
"""


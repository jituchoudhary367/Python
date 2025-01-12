list1 = ["Jitendra","Chaudhary"]
new_list = " ".join(list1) #joins the list elements with the space seperator.
print(new_list) #prints the joined list elements.

name = "Jitendra"
new_name = "{} Chaudhary".format(name) #joins the name with the string.
print(new_name)


""" conversion of string to the mutable data structure."""
my_string = "Jitendra,chaudhary"
new_list = list(my_string)
new_list[9]='C'
new_string = "".join(new_list)
print(new_string) #prints the modified string.


"""Python in operator"""
a = [3,54,64,564,74,53,4]
if 64 in a:
    print("True")
    
   
    
"""Repeated elements"""    
a = [3] * 9
b = [0] * 7
print(a) #output =>[3, 3, 3, 3, 3,3 , 3, 3, 3]
print(b) #output =>[0, 0, 0, 0, 0, 0, 0]
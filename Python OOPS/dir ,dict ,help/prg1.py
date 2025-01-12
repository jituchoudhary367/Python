"""
Dir 
"""
#Tuple
number = [93,84,39,29]  
print(dir(number)) #This will show all the methods available for the list object

print(number.__add__) #shows what the add method does and what it is
#If we need to check what is these methods doing, we can use help() function

#List
number = [93,84,39,29]
print(dir(number)) #This will show all the methods available for the list 


"""
Dict ==>> Converts any string into the Dictionary like the object : value
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1
        
p = Person("Jitu",39)
print(p.__dict__)    


"""
Help => 
"""    
print(help(Person))
        
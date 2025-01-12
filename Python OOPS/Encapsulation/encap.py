'''
Encapsulation :=> Encapsulation is the process of hiding the internal state of an object and requiring all interactions to be performed through an object’s methods ,
 encapsulation refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit.
1. Provides better control over data.
2. Prevents accidental modification of data.
3. Promotes modular programming
'''
#Public method
class Public:
    def __init__(self):
        self.name = "Jack" # public variable / attribute
    
    def display_name(self):
        print(self.name) #public method    
        
obj = Public()
obj.display_name() # calling public method
print(obj.name) # accessing public variable



#Protected
class Protected:
    def __init__(self):
        self.name = "Jitu"

class Subclass(Protected):
    def display_name(self):
        print(self.name)


ob = Protected()
ob.display_name()    
print(ob.name)             
        
class Animal:
    def __init__(self,name):
        self.name = name
    
    def make_sound(self):
        print(f"Sound made by the {self.name}")
        
    
class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name) #If we don't do this then also the output will be same
        self.name = name
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")
 
         
a =Animal("Dog") 
a.make_sound()
        
d =  Dog("Dog","Beagle")
d.make_sound()




#Example 2

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print(f"Sound made by the {self.name}")


class Cat(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="caracal")
        self.breed = breed    
        
        
    def make_sound(self):
        print("Meow!")
    
    
    
a = Animal("Cat","Caracal")              
a.make_sound()

c = Cat("Cat","corat") 
c.make_sound()           
    
            
          
    
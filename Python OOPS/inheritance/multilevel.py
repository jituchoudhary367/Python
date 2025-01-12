class Grandparent:
    def __init__(self,name,caste):
        self.name = name
        self.caste = caste
        
    def showDetails(self):
        print(f"Name : {self.name}")
        print(f"Caste : {self.caste}")    
        
class Parent(Grandparent):
    def __init__(self,name,parentname):
        Grandparent.__init__(self,name,caste="Chopra")
        self.name = name  
        self.parentname = parentname
        
    def showDetails(self):
        Grandparent.showDetails(self)   #Calling the parent class
        print(f"Parentname : {self.parentname}")    
        
class child(Parent):
    def __init__(self,name,age):
        Parent.__init__(self,name,parentname ="Vikram")          
        self.age = age
        
    def showDetails(self):
        Parent.showDetails(self)   #calling the parent class
        print(f"Age : {self.age}")      
        

c = child("Rohan",20)
c.showDetails()
print(child.mro())

        
        
        
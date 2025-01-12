class Parent():
    def __init__(self):
        self.value = "Inside Parent"
        
    def show(self):
        print(self.value)
        
class Child(Parent):
    def __init__(self):
        self.value = "Inside child"
        
    def show(self):
        print(self.value)           
        
ob1 = Parent()
ob2 = Child()

ob1.show()
ob2.show()



"""
Example 
""" 
# overriding in multilevel inheritance 
class Parent():  
    def display(self): 
        print("Inside Parent") 

class Child(Parent): 
    def show(self): 
      Parent.show(self) #if we want to print the statement of the parent class then only it is needed otherwise it will print the statement of the child class.
      print("Inside Child") 
    
class GrandChild(Child): 
    def show(self): 
        print("Inside GrandChild")         
    
g = GrandChild() 
g.show() 
g.display()       
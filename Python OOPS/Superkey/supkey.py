"""
super() => is used to refer to the parent class.

"""

class ParentClass:
    def parent_method(self):
        print("this is the parent method")
        
class childClass(ParentClass):
#     def parent_method(self):
#         print("Jitu")
#         return super().parent_method()
    
    def child_method(self):
        print("this is the child method")
        return super().parent_method()
    
child_ob = childClass()
child_ob.child_method()
child_ob.parent_method()
    
    
    
#Example
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id    
        
class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)   #super can be used to inherit the properties form the parent class and even using the constructor method can be inherited
        self.lang = lang 
        
emp1 = Employee("Jitu",490)
emp2 = Programmer("Jack",9090,"Python")
print(emp1.name,emp1.id)
print(emp2.name,emp2.id,emp2.lang)
        
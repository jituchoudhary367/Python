class Employee:
    def __init__(self,name):
        self.name = name
        
    def show(self):
        print(f"The name of the Employee is : {self.name}")
           

class Dancer:
    def __init__(self,dance):
        self.dance = dance
        
    def show(self):
        print(f"The name of the dance is : {self.dance}")  
          
class DancerEmployee(Employee,Dancer):  #Here if the order of the parent class is changed then it will print the output of the first parent class
    def __init__(self,dance,name):
        self.dance = dance
        self.name = name


d = DancerEmployee("Bharatnatyam","Shivani")
print(d.name,d.dance)   
d.show()    
print(DancerEmployee.mro())  #here also the first parent will be shown first then the second parent will be shown       
    
    
    
    
    
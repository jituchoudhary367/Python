"""Inheritance :- is a property that child class inherit from the parent class in any function and methods.This can be in any type of section like Public , private, protected.


"""
class employee:     #This is the parent class and all the properties can be inherited from this class to any of the child class.
    def __init__(self,name,id, salary, age):
        self.name = name
        self.id =id
        self.salary = salary
        self.age = age
        
    def showDetails(self):
        print(f"The name of the employee :{self.name} and the id :{self.id} is having salary {self.salary} Rs.He is about {self.age} years.")    

class Programmer(employee):  #This is the child class and all the properties can be inherited.
    def showLanguage(self):
        print("The language is Python")    

class JrProgrammer(employee):
    def __init__(self,name,id):
        self.id = id
        self.name = name
                    
    def showDet1(self):
        print(f"The name of the programmer : {self.name} and the id is : {self.id}")                
        
emp1 = employee("Jack","120021",340000,34)
emp1.showDetails() 
emp1 = Programmer("John",120022,455000,43)
emp1.showDetails() 
emp1.showLanguage()

emp2 = JrProgrammer("Robert",120023)  
emp1.showDetails()
emp2.showDet1()
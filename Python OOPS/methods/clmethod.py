class Employee:
    company = "Google"
    def show(self):
        print(f"The name is : {self.name} and the company is : {self.company}") 
    
    def changeCompany(cls,newCompany):
        cls.company = newCompany
        
e1 = Employee()
e1.name = "Jitendra"
e1.show() # Output: The name is : Jitendra and the company is : Apple
e1.name = "John"
e1.changeCompany("Apple")
e1.show() 

print(Employee.company)    #Here the fianl output is Apple 


"""
Check the program once to check that why the last company name is not changing.
"""
#If we want to change the company name then we need to use the class method as the decorator then the last output will change.
class Employee:
    company = "Google"
    def show(self):
        print(f"The name is : {self.name} and the company is : {self.company}") 
    @classmethod
    def changeCompany(cls,newCompany):
        cls.company = newCompany
        
Employee() #this can be called in this way as the function
#e1 = Employee() ==> This will also do the same 
e1.name = "Jitendra"
e1.show() # Output: The name is : Jitendra and the company is : Apple
e1.name = "John"
e1.changeCompany("Apple")
e1.show() 

print(Employee.company)       
    
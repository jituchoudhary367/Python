class Employee:
    company_name = "ABC Corporation" #This is the class variable which is associated to the class.
    noOfEmployee = 0
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.03
        Employee.noOfEmployee +=1
    #If we don't add self in the below function then it will throw error.    
    def showDetails(self):
        print(f"The name of the Employee {self.name} in {self.company_name} sized with the emp {self.noOfEmployee} and the raise amount is {self.raise_amount}")
    
#Employee.showDetails(emp1)           
emp1 = Employee("Jitendra")
emp1.raise_amount = 0.04 #The values can be changed here alsi because it is instance variable which is not associated with any of the class .they are related to the instance of the class.
emp1.company_name = "ABC Corporation India" # this is instance var so it just changed for the "Jitendra" only.
emp1.showDetails()

Employee.company_name = "BDC Group"
print(Employee.company_name)

emp1 = Employee("John")
emp1.company_name= "BDC Group India" 
emp1.showDetails()
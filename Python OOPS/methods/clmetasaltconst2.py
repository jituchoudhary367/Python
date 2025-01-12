class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        
    @classmethod        #For this method we have to use the same type if the seperator otherwise it will throw the error
    def Fromstr(cls,string):
        return cls(string.split("~")[0],int(string.split("~")[1]))
    
string = "Jitu~30" 
person = Person.Fromstr(string)
print(person.name,person.age)
     
        
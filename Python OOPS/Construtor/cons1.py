#Constructor is a method in a class used to create and initialize an obejct of the class.
#A constructor is a unique function that gets called automatically wwhen an object is created of a class.
"""
There are two type of the constructor:-
1.Parameterized constructor :- when the constructor accepts the parameter along with the self.
2.Default constructor :- when doesn't take any kind of the parameters.

"""
#This is the example of the Parameterized constructor.
class Person():
    def __init__(self,n,o,a): #This is a constructor
        print("Hello , Everyone")
        self.name = n  #these are the objects 
        self.occ = o
        self.age = a
    
    
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a = Person("Arjun","Developer",49)  #Here the calling pararmeters should be n-1 of teh constructor because constructor is containing one parameter named self which doesn't need to called.              
b = Person("Ram","HR",34)     
c = Person("Anil","Accountant",39) 
a.info()
b.info()
c.info()


#This is the example of the Default constructor.
class Person():
    def __init__(self): #This is a constructor
        print("Hello , Everyone")
    
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a = Person()  #Here the calling pararmeters should be n-1 of teh constructor because constructor is containing one parameter named self which doesn't need to called.              
b = Person()     
c = Person() 
# a.info()
# b.info()
# c.info()     
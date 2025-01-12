"""
--->>> These are used for the Encapsulation.
Getter :- Getter in python are the methods that are used to access the values of an object's properties.
=>They are used to retrun the value of specific property,and are typically defined usnig the @property decorator.

Setter :- The setter is a method that is used to set the property's value. 
=>It is very useful in object-oriented programming to set the value of private attributes in a class and declared as @property.setter
"""


class Myclass:
    def __init__(self,value):
        self.value = value
    
    
    def show(self):
        print(f"value is {self.value}")   
    
    #This is getter method    
    @property
    def ten_value(self):
        return 10*self._value 
    
    #This is the setter method
    @ten_value.setter
    def ten_value(self,new_value):
        self._value = new_value/10
    
obj = Myclass(10) 
obj.ten_value = 539
print(obj.ten_value)
obj.show()       
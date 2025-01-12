class shape:
    def __init__(self,x,y):
        self.x = x 
        self.y = y
    
    def area(self):
        return self.x * self.y 
    
    def perimeter(self):
        return 2 * (self.x + self.y)
    
    def area(self):
        return 3.14 * (self.x * self.y)
    
rec = shape(34,6)
print(rec.area())

rec1 = shape(34,5)
print(rec1.perimeter())

print("\n")

"""
# class Circle:
#     def __init__(self,rad):
#         self.rad =rad
    
#     def area(self):
#         return 3.14 * self.rad * self.rad       

# c = Circle(49)
# print(c.area())     
"""


#This is using inheritance 
class Circle(shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius,radius)  
        #If we write upto here only then it will not print the area as the exact it will be using above circle class
        
    def area(self):
        return 3.14 * super().area()   
        
c = Circle(49)
print(c.area())                   
#static methods :- methods in python that belongs to class not to instance of the class.
#If we want to call a method in the class then not necessary to pass self argument.
 
class Maths:
    def __init__(self,num):
        self.num = num
        
    def addtonum(self,n):
        self.num = self.num +n
        
    @staticmethod
    def add(a,b):
        return a+b
   
result = Maths.add(1,3)
print(result)  # Output: 4

a = Maths(5)
print(a.num)  # Output: 5

a.addtonum(5)
print(a.num)
       
#so the static method can be accessed from the instance of the class and even from the class name also       
print(a.add(25,65))
print(Maths.add(65,99))       
            

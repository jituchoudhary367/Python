#Decorator is a powerful and versatile tool that allow you to modify functions and methods.
#Decorator is used just before defining the function
def greet(fx):
    def mfx():
       print("Good Morning")
       fx()
       print("Thanks for using this function")
    return mfx

# @greet

def hello():
    print("Hello world")

greet(hello)()   #This  
# hello()

@greet
def add():
    print("The sum is :",x+y)   

x = int(input("Enter the number1:"))
y = int(input("Enter the number2:"))  

add()  
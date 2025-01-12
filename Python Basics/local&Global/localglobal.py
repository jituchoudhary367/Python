x = 48
print(x)

def funct():
    x=45
    print("The local x is : ",x)
    
funct()    
print("The global x is : ",x)    



print("\n")
#Exp 2
x = 40
print("The value of x is : ",x)

def func1():
    global x     #global keyword is used to declare the variable as global which can be accessed inside the function
    x = 30
    y = 48
    print("The value of y is : ",y)
    
    
func1()
print("The value of x is : ",x)
# print("The value of y is : ",y)    #It will give an error because y is not defined in the global scope.It is a local variable in the function func1().
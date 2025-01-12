#Finally is used to execute a block of code if the try block does not raise an exception. If an exception either the try block is executed or the except block is executed The finally keyword containded statemnent is always executed
def func1():
    try:
        l={1,45,6,6,4}
        i = int(input("Enter the index:"))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("This statement is always executed.")
        #print("This statement is always executed.") 
        
func = func1()
print(func)    
     
"""
So the basic difference between the first and second program is use of finally with and without the function
In the case of not using the functon we can use the commented print statement to print the statement at the end of the program it wil always executed either the try bock is executed or the except block is executed and the finally is always executed.
If the finally statement is used in the function then it is always executed whether the try or the except block is executed but if we use the commented print statement in the function it is not executed in that scenario.
"""     
     
try:
    l={1,45,6,6,4}
    i = int(input("Enter the index:"))
    print(l[i])
except:
    print("Some error occured")
finally:
        print("This statement is always executed.")
        #print("This statement is always executed.")      
     
#Check the in-built errors on internet     
     
           
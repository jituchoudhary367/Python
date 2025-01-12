# def average(a,b):
#     print("The average is : ",(a+b)/2)
    
# a=44
# b=43
# average(a,b)   
# a=44930
# b=9495
# average(a,b)

def average(*numbers):  #considering it as a tuple
    print(type(numbers))
    sum =0
    for i in numbers:
        sum = sum +i
        print("Average is:",sum/len(numbers))
average(49,93)       #for thr first number it is calculating the averge and then for the second number 
                     #it is again calculating the average but in this case it is adding the averge of number1 in number2 

#values should be in sequence 
def average(a,b,c=2):
    print("The average is : ",(a+b+c)/2)
a=44
b=43
average(a,b)

   


def name(fname ,mname="John",lname="whatson"):
    print("Hello,",fname,mname,lname)
name("Karl") 
name("Amy","Lauren","Paul")   



"""
Function using return statement
    """

def average(*numbers):  #considering it as a tuple
    print(type(numbers))
    sum =0
    for i in numbers:
        sum = sum +i
#         print("Average is:",sum/len(numbers))
# average(49,93)
    return sum/len(numbers)
#returns the value to the finction back
c = average(4,5,7,8,4)
print(c)
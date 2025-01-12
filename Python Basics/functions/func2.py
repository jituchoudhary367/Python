# a = 9
# b = 43
# gmean = (a + b)/2
# print(gmean)

def CalculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)    
def isGreater(a,b):
  if(a>b):
    print(f"First number {a} is greater.")
  else:
    print(f"Second number {b} is greater.")  

# def islesser(a,b):  if only this much part is defined then it'll show error    
      
# def islesser(a,b):
#     pass  #pass is used to proceed further if the body of the function is not given and it'll will not show any kind of error
a=4
b=44
CalculateGmean(a,b)
isGreater(a,b)
    
#built in function => not need to define max(),min(),range() etc.


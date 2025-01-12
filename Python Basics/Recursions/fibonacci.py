def fibonacci(n):
    if(n<=1):
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
    
nterm = int(input("Enter number of terms :"))

# check if the number is valid or not 
if nterm<=0:
    print("The term entered is invalid.")
else:
    print("Fibonacci series is:")
    for i in range(nterm):
        print(fibonacci(i))        
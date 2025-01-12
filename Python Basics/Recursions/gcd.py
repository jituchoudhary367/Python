def gcd(n1,n2):
    if(n2==0):
        return n1
    else:
        return gcd(n2,n1%n2)
 
n1 = int(input("Enter the number n1 :"))
n2 = int(input("Enter the number n2 :"))       
print("The GCD of the number n1 and n2 is :",gcd(n1,n2))         
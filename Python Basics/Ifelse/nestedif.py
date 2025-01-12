num = int(input("Enter the number:"))
print("The number is : ",num)

if(num<0):
    print("The number is negative.")
elif(num>0):
    if(num<10):
        print("The number is single digit number.")
    elif(num>=10 & num<100):
        print("The number is double digit number.")
    else:
        print("The number is three digit pr greater.") 
else:
    print("The numbe is zero.")                  
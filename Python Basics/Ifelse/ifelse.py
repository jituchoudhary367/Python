num1 = int(input("Enter the number1 : "))
print("The num1 is : ",num1)
num2 = int(input("Enter the number2 : "))
print("The num2 is : ",num2)
num3 = int(input("Enter the number3 : "))
print("The num3 is : ",num3)

if(num1>num2 & num1>num3):
    print("The greatest number is : ",num1)
elif(num2>num1 & num2>num3):
    print("The greatest number is : ",num2)  
else:
    print("The greatest number is : ",num3)
          
x = int(input("Enter the value of x : "))

match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!= 80:
        print(x , "is not 80")
    case _ :
        print(x)               

#it checks only for the first condition if not match then results whatever is there
#in this case if we enter the number 45 then it shows that 45 is not 90
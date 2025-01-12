num = input("Enter the number :")
print(f"Multiplication table of {num} is :")

try:
   for i in range(1,11):
       print(f"{int(num)} X {i}={int(num)*i}")
except Exception as e:
#or can write at it's place { except: }    
    # print(e) can use this also at the place of the below print statement
    print("Some unexpected error occured.")
    
print("Some imporantant lines of the code")
print("End of the program")

"""
1.Here if input is given as the number then it will print the table of that number 
2.But if the input is given as invalid data type like string or anything else then it will raise the exception


"""

#Python have some inbuilt Exception case to handle the error or the exception

try:
    num = int(input("Enter the number : "))
    a = [0,5]
    print(a[num])
except ValueError:
    print("Number entered is not a integer.")
except IndexError:
    print("Index Error")    
        
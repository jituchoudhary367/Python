a = 94
b = 49
print(a is b) #is is used for checking the location 
print(a==b) #It just compare the value that values are equal or not

a = "Jitu"
b = "Jitu"   #strings are case sensative
print(a is b)
print(a==b)

a = [2,4,56,7,5]  #here both the lists contains the same values but they are mutable that is why the "is" is showing false but if we use the list containing the same values then it will show true because lists are immutable.
b = [2,4,56,7,5]  #but the "==" is resulting True Because it doesn't checks the location , just compares the values
print(a is b)
print(a==b)

a = (2,4,56,7,5)  #here both the lists contains the same values but they are mutable that is why the "is" is showing false but if we use the list containing the same values then it will show true because lists are immutable.
b = (2,4,56,7,5)  #but the "==" is resulting True Because it doesn't checks the location , just compares the values
print(a is b)
print(a==b)


#Example
class Sum:
    def display(self,a = None,b=None):
        if a is not None and b is not None:
            print("The sum is :",a+b)
        elif a is not None:
            print(a)
        else:
            print("Nothing to display")

ob = Sum()
ob.display()
ob.display(39)
ob.display(38,48)                
            
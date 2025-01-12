#Walrus Oprerator is represented by the (:=) syntax and can be used in a variety of contexts including while loops and if statements. The Walrus Operator is a new feature in Python 3.8 and later versions.
numbers = [1, 2, 3, 4, 5]

while(n := len(numbers))>2:
    print("The number popped is :",numbers.pop())
    
    print(numbers)
    
#Program without Walrus opertor
# cars = list()
# while True:
#     car = input("Enter a car (Q to quit): ")
#     if car.upper() == 'Q':
#         break
#     cars.append(car)
"""
Now the implementation of the above number with the wlarus operator
"""    
cars = list()
while (car := input("Enter the name of the car:")) != "Q":
    cars.append(car)
    
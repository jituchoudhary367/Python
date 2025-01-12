#Tuples => Values of the tuples can't be changed 
tup = (1,48,43,56,768,45)
#tup[0]=90 if we want to add more values to tuple can't add anymore
print(type(tup),tup)
print(tup[0])
print(tup[-1])
print(tup[2])
#print(tup[33]) invalid we can't access indices that is not present in tuple

if 56 in tup:
    print("Yes , 56 is in tuple")
else:
    print("56 is not in tuple")    
    
tup2 = tup[1:4]    #tuple assigment is possible
print(tup2)



"""Creating tuple"""
Tuple1 = () #empty tuple
print("Initial empty Tuple: ",Tuple1)
Tuple1 = ('Geeks', 'For')    # with the use of string
print(Tuple1)
list1 = [1, 2, 4, 5, 6]    # the use of list
print(tuple(list1))
Tuple1 = tuple('Geeks') # with the use of built-in function
print(Tuple1)
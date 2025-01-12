tuple1 =(0,3,5,6,7,2,58,3,5,5,2,2,7,9,45,6,87,34,7,9,7,54,33)
print(type(tuple1))
print(len(tuple1))
res = tuple1.count(3)
print("count of 3 in tuple1 is :",res)
res = tuple1.index(7)
print("Index of the tuple1 is : ",res)
res = tuple1.index(7,13,20) # where 7 is the element to search and the 13,20 are the starting and end position
print("Index of the tuple1 is : ",res)
#MAP
def cube(x):
    return x*x*x
print(cube(5))

# l = [1,2,4,3,5,8,6]
# newl = []
# for item in l:
#     newl.append(cube(item))
    
# print(newl)    

#using map for the above example
l = [1,2,4,3,5,8,6]
newl = list(map(cube,l))
newl = list(map(lambda x: x*x*x,l)) #if we use this there is no need to define the cube function
print(newl)

#FILTER
def filter_function(newl):
    return newl>54

newnewl = list(filter(filter_function,newl))
print(newnewl)


#REDUCE
from functools import reduce

number = [5,4,8,9,6,4,9,9,6]
newl = reduce(lambda x,y: x+y,number)
print(newl)


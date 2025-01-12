l =[1,34,6,77,89,1,3,5,7,43,24,5,6,43,2,4,56,4,2,1,3,34,7]
print(l)
# l.append(73)
# l.sort(reverse=True)

# l.reverse()
# print(l.index(1))
# print(l.count(1))

# m=l.copy()
# m[0]=0
l.insert(1,490)
m=[303,404,505]
l.extend(m)
print(l)

k=l+m
print(k) 


"""Adding Elements into List
=====================================
1. append(): Adds an element at the end of the list.
2. extend(): Adds multiple elements to the end of the list.
3. insert(): Adds an element at a specific position.

"""
a = []
a.append(10)   #adds the element at the end of the list
print("After append(10):", a)  #=> [10]
a.insert(0, 5) #adds the element at the specified position
print("After insert(0, 5):", a)  #=> [5, 10]
a.extend([15, 20, 25])  # Adding multiple elements  [15, 20, 25] at the end
print("After extend([15, 20, 25]):", a)  #=> [5, 10, 15, 20, 25]
a[2] = 40
print(a)  #=> [5, 10, 40, 20, 25]



"""Removing Elements from List 
=====================================
1. remove(): Removes the first occurrence of an element.
2. pop(): Removes the element at a specific index or the last element if no index is specified.
3. del statement: Deletes an element at a specified index.
"""
a.remove(40)  
print("After remove(40):", a) #=> [5, 10, 20, 25]
popped_val = a.pop(1)  
print("Popped element:", popped_val) #=> 10
print("After pop(1):", a) # => [5, 20, 25]

del a[0]  
print("After del a[0]:", a) #=> [20, 25]


"""Iterations of the lists""" #Iteration => Access the elements one by one.
a = ['apple', 'banana', 'cherry']
for item in a:
    print(item)
    
    
 
"""Nested lists"""
a = [
  [49,45,64],
  [44,48,97],  
  [30,35,6]  
]    
print(a[2][2])  #=> 6  (the index starts form 0)
print(a[0][1])  #=> 45 
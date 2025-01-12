s1 = {2,3,4,56,7,78,9,3}
s2 = {34,4,56,78,4,3,4,66,6,5,4,3}
s1.update(s2) #Update =>it updates the values in the set which is not present in that set from the set we want to update 
#it adds the value in the set first form the set second which is not present in set first 
print(s1.union(s2))
print(s2.union(s1))

s1.update(s2) 
print(s1.intersection(s2))
print(s2.intersection(s1))

#symmetric difference => Values which is not present in the another set
s3 = s1.symmetric_difference(s2)
print(s3)

#Some other methods
s1 = {2,3,4,5,6,7,8,9}
s2 = {3,4,5,6,7}
print(s1.isdisjoint(s2))  # It checks whether the first set is not containing any of the element of the another set then it'll return Boolean values
print(s2.issubset(s1))
print(s1.issuperset(s2))

s1.add(10) #add values in the set 
print(s1)

#remove and Discard
s1.remove(10)
#s1.remove(10)  if element is not there then it will throw the error
s1.discard(10) #It will not throw the error even if there the element is not present the set
print(s1)


#pop => returns the last value of the set it can be any value not necessary that it will pop the last written element it is random 
item = s1.pop()
print(item)
print(s1)

#clear => It is used to delete the particular item values not the entire set
s1.clear()
print(s1)

#del => it is used to delete the entire set
del s1
#print(s1) => it will show the error






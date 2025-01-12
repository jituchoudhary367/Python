#It returns true if all the elements are true and returns false if one or more than one and all the elements are true.
#for the lists
l = [33,5,7,8,89,9]
print(all(l))  #=>True
l = [0,0,False,0,False]
print(all(l))  #=>False
l = [1, 0, 6, 7, False]
print(all(l))   #=>False
l = []
print(all(l)) #=>True
l = [1,-3,0,2,4]
print(all(ele > 0 for ele in l)) #=>False

#For the sets
s = {1, 1, 3}
print(all(s))  #=>True
s = {0, 0, False}
print(all(s)) #=>False
s = {1, 2, 0, 8, False}
print(all(s)) #=>False
s = {}
print(all(s)) #=>True

#for the dictionaries
d = {1: "Hello", 2: "Hi"}
print(all(d)) #=>True
d = {0: "Hello", False: "Hi"}
print(all(d)) #=>False
d = {0: "Salut", 1: "Hello", 2: "Hi"}
print(all(d)) #=>False
d = {}
print(all(d)) #=>True

#For the Strings
s = "Hi There!"
print(all(s)) #=>True
s = "000"
print(all(s)) #=>True
s = ""
print(all(s)) #=>True
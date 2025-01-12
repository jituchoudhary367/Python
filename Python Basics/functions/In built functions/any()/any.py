#if any of the values is true then it will returns true
#For the list
l = [False, False, True, False, False]
print(any(l)) #=>True
l = [4, 5, 1]
print(any(l)) #=>True
l = [0, 0, False]
print(any(l)) #=>False
l = [1, 0, 6, 7, False]
print(any(l)) #=>True
l = []
print(any(l)) #=>False

#For the tuples
t = (2, 4, 6)
print(any(t)) #=>True
t = (0, False, False)
print(any(t)) #=>False
t = (5, 0, 3, 1, False)
print(any(t)) #=>True
t = ()
print(any(t)) #=>False

#for the dictionaries
d = {1: "Hello", 2: "Hi"}
print(any(d)) #=>True
d = {0: "Hello", False: "Hi"}
print(any(d)) #=>False
d = {0: "Salut", 1: "Hello", 2: "Hi"}
print(any(d)) #=>True
d = {}
print(any(d)) #=>False

#For the Strings
s = "Hi There!"
print(any(s)) #=>True
s = "000"
print(any(s)) #=>True
s = ""
print(any(s)) #False
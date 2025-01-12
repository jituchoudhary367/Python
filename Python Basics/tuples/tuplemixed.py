"""Mixed data type tuples"""
tuple1 = (5,'Jitendra',3,4,"tony")  #with mixed data type
print(tuple1)
tuple1 = (5,3,4,5,6,7,8,9)  #with nested tuples
tuple2 = ("Lion,Deer,Dog")
tuple3 = (tuple1,tuple2)
print(tuple3)
tuple1 = (3)*4  #tuple with repitition
print(tuple1)
tuple2 = ("king")
n = 4
for i in range(int(n)):
    tuple2 = (tuple2 ,"king")
    print(tuple2)
    
    
    

"""Accessing Tuple"""    
tuple1 = tuple("BMW")  #if we use tuple in front then only one string can be passed and it seperates each letter with comma.
print(tuple1) 
tuple1 = ("BMW","Lamborghini","Audi","Rolls Royce","Msareti")
a,b,c,d,e = tuple1
print(a ,b ,c ,d ,e)  #unpacking tuple
tuple1 = (0,1,2,3,4,5)
tuple2 = (6,7,8,9,10)
tuple3 = tuple1 + tuple2  #adding two tuples (Applicable for the tuple1 and tuple2 are of the different data type(int and strings))
print(tuple3)
del tuple3
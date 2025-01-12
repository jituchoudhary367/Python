list = [1,2,3,4,5,6,7,8,9,10,"Jitendra","chaudhary"]
print(list)
print(type(list))
print(list[2])
print(list[4])
print(list[5])
print(list[10])

print(list[-4]) #negative index 
print(list[len(list)-4])  #positive index converson to avoid confusion
print(list[12-4])


#same thing applies for all number ,strings
if "Jitendra" in list:
    print("Yes")
else:
    print("No")    
    
    
print(list)
print(list[1:-1])
print(list[1:11:3]) #from 1 to 11 sliced and then gap of 2 for every element and then next 3rd element is printed  

#list comprehension
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)


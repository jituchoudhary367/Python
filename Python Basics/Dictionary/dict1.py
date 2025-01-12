dic={
    344: "Jitendra",
    34 : "Jack",
    495: "Tony"
}
print(dic[344])




dict1 = {
    'name' : "Jitendra", 'age' : 20 , 'eligible' : True 
}
print(dict1)
print(dict1.keys())
print(dict1.values)
for key in dict1.keys():
   # print(dict1.keys)
    print(f"The value corresponding to the key {key} is : {dict1[key]}")

print(dict1.items())
for key , value in dict1.items():
   print(f"The value corresponding to the key {key} is : {value}")
for i in range(5):
    if i==0:
        break
    print(i)
else:
    print("Value is out of the range")    
    
    
for i in range(5):
    print(i)
    if i==4:
        break
else:
    print("Value is out of the range")        
    
    
for x in range(4):
    print("Iteration number {} in for loop",format(x+1))

else:
    print("Else block in loop")

print("Out of the loop")        
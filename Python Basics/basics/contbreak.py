for i in range(12):
    print("5 X",i+1, "=",5*(i+1))
    if(i==10): #here it will execute the i=10 till it will not go to 11 it will not terminate
        break
    
print("loop is terminated")    

#Starts from 0 and terminates at 10
for i in range(12):
    if(i==10):  # here when it is hitting 10 it will terminate directly.
        break
    print("5 X",i+1, "=",5*(i+1))
    
print("loop is terminated")    


#continue => when the codition is matching it'll directly skip the current iteration and go for the next one
for i in range(12):
    if(i==10):  # here when it is hitting 10 it will terminate directly.
        print("Skip the iteration")
        continue
    print("5 X",i+1, "=",5*(i+1))
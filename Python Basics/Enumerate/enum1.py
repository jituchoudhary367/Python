marks = [12,45,43,57,97,6,54,35,76]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index==4):
#         print("Awesome performance ! 'Jack'")
#     index +=1    

#use of enumerate
"""
If the index is not given the function enumerate() then it will start from 0 and will increment by 1 in each iteration.
and the index can be given manually also from the index we need to start
"""
for index,mark in enumerate(marks,start=0):
    print(mark)
    if(index==4):
        print("Awesome performance ! 'Jack'")
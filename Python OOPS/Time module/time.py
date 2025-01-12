#Time module in Python provides a set of work with time-related operations , such as timekeeping , formatting ,and time conversions.

import time
# def usingWhile():
#     i = 0
#     while i< 50000:
#         i = i+1
#         print(i)


# def usingFor():
#    for i in range(50000):
#        print(i)

# init = time.time()   #It is standard time that is mentioned on python.org 
# usingWhile()
# print(time.time()-init)  #shows the time needed for the execution.
# init = time.time()
# usingFor()
# print(time.time()-init)   



#example 2
# print("Hello Brother What are you doing.")
# time.sleep(4)  #It waits for the time defined in the function.
# print("This statement is executed after 4 seconds") 



#example 3
t = time.localtime()
formatted_time = time.strftime("%Y-%M-%D %H-%M-%S",t)
print(formatted_time)


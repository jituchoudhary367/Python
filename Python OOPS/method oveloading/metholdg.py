# def add(a,b):
#     return print(a+b)


# def add(a,b,c):    
#     return print(a+b+c)

# #this is calling the function 2 that is consisting of the three parameters and overriding the method that is consisting of the two parameters only
# add(4,6,7)


#Example 1
#The asterisk (*) before args allows you to pass any number of positional arguments to the function.

# def add(datatype,*args):
    
#     if datatype == 'int':
#         answer = 0
        
#     if datatype == 'str':
#         answer = ''
        
#     for x in args:
#         answer = answer + x 
        
#     print(answer)
    
# add('int',4,6,7,8,89,9)
# add('str','Hi ',"Jitendra ","What ",'are ','you ',"doing.")  

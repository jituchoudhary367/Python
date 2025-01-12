# def multiple(x):
#     return x*3
# print(multiple(5))

#lambda function is used to shorten the short program and there is no headache of indentation
#lambda function can take multiple values 
multiple = lambda x: x*4
print(multiple(5))

cube = lambda x: x*x*x
print(cube(48))

avg = lambda x,y,z: (x+y+z)/3
print(avg(4,56,7))

#hence this can be applied to the functions also
def appl(fx,value):
    return 6 + fx(value)
#these both the print statement given below is same
print(appl(cube,3))
print(appl(lambda x: x*x*x,3))



#another example
def funct(f,number):
    return 6*f(number)

print(funct(cube,4))
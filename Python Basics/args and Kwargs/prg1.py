def Mysum(*args):
    return sum(args)

print(Mysum(34,53,43,43,3,23,4,3))


def Mysum(**kwargs):   #The Type of the kwargs is a dictionary
    return sum(kwargs.values())
print(Mysum(a=34,b=53,c=43,d=43,e=3,f=34))
#Hybrid Inheritance

class A:
    pass 

class Baseclass(A):
    pass 

class baseclass(A):
    pass

class Derived(Baseclass,baseclass):
    pass



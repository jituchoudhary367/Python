class vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
        
    def __str__(self):
        return f"({self.i}i + {self.j}j + {self.k}k)"
    
    # def __add__(self,x):   #This results in string
    #     return f"({self.i + x.i}i + {self.j+x.j}j + {self.k+x.k}k)"
    
    #this results in Vector
    def __add__(self,x):
        return vector(self.i + x.i , self.j+x.j ,self.k+x.k)
        
        
v1 = vector(4,45,6)
print(v1)        

v2 = vector(1,2,3)
print(v2)

print(v1+v2)
print(type(v1+v2)) # return f"({self.i + x.i}i + {self.j+x.j}j + {self.k+x.k}k)" ==>> This will return the type string but the vector addition must be of the vector type for that creating the vector type
        


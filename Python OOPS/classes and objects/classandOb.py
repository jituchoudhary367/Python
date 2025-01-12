class Person:
    name = "Jitu"
    occupation = "Software Developer"
    age = 38
    networth = 4900000
    def info(self):
        print(f"{self.name} is a {self.occupation}.He has a networth of {self.networth}$")
    
p = Person()  
q = Person()
r = Person()
p.name = "Jitendra"
p.occupation = "CEO"
p.age = 34
p.networth = 8900000

q.name = "John"
q.occupation = "Senior Developer"
q.age = 54
q.networth = 800000
print(p.name,p.age,p.networth,sep="||")
print(q.name,q.age,q.networth,sep="||")
p.info() 
q.info()
r.info()
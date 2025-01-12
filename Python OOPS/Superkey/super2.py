class Parent():
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
    def show(self):
        print(self.name,self.id)
    
class Child(Parent):
    def __init__(self,name,id,phno):
        super().__init__(name,id)
        self.phno = phno
        
    def show(self):
        print(self.name ,self.id ,self.phno)
        
ob = Child("Jack","499494",9922939933)
ob.show()
                            
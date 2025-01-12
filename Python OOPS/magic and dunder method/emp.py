class Employee:
    name = "Jitendra"
    def __len__(self):
        i = 0
        for i in self.name:
            i = i + 1
            return i
    
    def __str__(self):
        return f"The name of the employee is : {self.name} (str)"
    
    def __repr__(self):
        return f"The employee is : {self.name} (repr)"        
    
    def __call__(self):
        print("hello I'm Good")   
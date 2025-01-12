class Employee:
    name = "Jitendra"
    def __len__(self):
        i = 0
        for i in self.name:
            i = i + 1
            return i
        
        
emp = Employee()
print(emp.name)
print(len(emp.name))        
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
    
    
    
#Example 2
class Car:
    def company(self):
        print("The parent company is volkswagon")
        
    def specification(self):
        print("The company designs luxury comapanies")
        
class Lambo(Car):
    def model(self):
        print("Lamborghini model Urus is very luxury and comfortable")
        
class Audi(Car):
    def model(self):
        print("Audi R8 is very luxury and comfortable")        

obj_car = Car()
obj_lambo = Lambo()
obj_audi = Audi()

obj_car.company()
obj_car.specification()

obj_lambo.company()
obj_lambo.model()

obj_audi.company()
obj_audi.model()
    
                    
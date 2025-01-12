letter = "Hey ! my name is {} amd I'm from {}."  #these indexes can be in any form
country ="India"
name = "Jitendra"

print(letter.format(name , country))

#This is called fstring and this can be written in any format and any order
letter = "Hey ! my name is {} amd I'm from {}."  
country ="India"
name = "Jitendra"

print(f"Hey ! my name is {name} amd I'm from {country}")
print(f"Hey ! my name is {{name}} amd I'm from {{country}}") #This is used to add {}

#another example
price = 2859.59458499
msg = f"For only {price:.2f} rs!"
print(msg)

print(type(f"{2*30}"))
a = "Jitendra Jitendra Chaudhary  "
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Jitendra","Jack"))
print(a.split(" "))
blogHeading = "introduction to Javascript"
print(blogHeading.capitalize())

str1 ="welcome to Python console!!!"
print(len(str1))
print(str1.capitalize())
print(len(str1.center(50)))
print(a.count("Jitendra"))
print(str1.endswith("!!!"))
print(str1.endswith("to",4,10))

str2 = "He name is Dane. He is an honest man."
print(str2.find("is"))
# print(str2.index("isjh"))

print(str2.isalnum())
str2 ="Welcometo0000"
print(str2.isalpha())
print(str2.islower())

str3 = "Jitendra chaudhary" #str3 = " Jitendra Chaudhary#$@@#$"
print(str3.isprintable())   #print(str3.inprintable())  ==> returns false beacuse contains the special character
str3 = "         " #Using spacebar
print(str3.isspace())
str3 = "    " #Using tab
print(str3.isspace())

print(str3.istitle())
print(str3.startswith("Jitendra"))
print(str3.title())





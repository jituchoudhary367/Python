"""For the integers """
x = 5
y = 43.45
z = 5j
print(type(x))
print(type(y))
print(type(z))
res = 5+5
res = 590-53
res =4*5
res = 5/2  #=> Output : 2.5
res = 5//2 #=> Output : 2
res = 2 ** 3 #Exponentiation (**) => Output : 8
res = abs(-10) #Absolute Value (abs) => Output : 10
res = round(3.14159, 2)  # Output: 3.14 (rounds to 2 decimal places)


"""For the float"""
res = 3.5 + 2.2   # Output: 5.7
res = 7.8 - 4.3   # Output: 3.5
res = 5.5 * 2.0   # Output: 11.0
res = 9.0 / 4.5   # Output: 2.0
res = 9.0 // 4.5  # Output: 2.0 (it returns the truncated quotient)
res = 9.0 % 4.5   # Output: 0.0 (remainder when divided)
res = 2.5 ** 2    # Output: 6.25 (2.5 raised to the power of 2)
res = abs(-7.4)   # Output: 7.4 (absolute value)
res = round(3.14159, 2)  # Output: 3.14 (rounds to 2 decimal places)


'''For the Complex number'''
res = (3 + 4j) + (1 + 2j)   # Output: (4 + 6j)
res = (5 + 6j) - (2 + 3j)   # Output: (3 + 3j)
res = (2 + 3j) * (1 + 4j)   # Output: (-10 + 11j)
res = (8 + 6j) / (2 + 3j)   # Output: (2.0 + 0.0j)
res = (1 + 1j) ** 2    # Output: (0 + 2j) (raises the complex number to the power of 2)
res = abs(3 + 4j)   # Output: 5.0 (absolute value of a complex number, which is sqrt(3^2 + 4^2))
res = (3 + 4j).conjugate()   # Output: (3 - 4j) (negates the imaginary part)
real = (3 + 4j).real   # Output: 3.0
imag = (3 + 4j).imag   # Output: 4.0


'''Type conversion'''#Using Built-In Function
a = 2
print(float(a)) # Output: 2.0
b = 5.6
print(int(b)) # Output: 5
c = '3'
print(type(int(c))) # Output: <class 'int'>
d = '5.6'
print(type(float(c))) # Output: <class 'float'>
e = 5
print(complex(e)) # Output: (5+0j)
f = 6.5
print(complex(f)) # Output: (6.5+0j)
#Using Arithmetic Operations: 
a = 1.6
b = 5
c = a + b
print(c)
print(("\n"))


"""for the random numbers"""
import random
random_number = random.randint(1,100)  # Output: a random float between 0.0 and 1.0
print("The number generated is : ",random_number)


""" Special type of numbers"""
#nan = Not a Number and is used to represent undefined or unpresentable value such as dividing 0 by 0
#infinity and -Infinity => In Python it can be represented as "Inf" and "-Inf" respectively.
# NaN Example
import math
print(math.nan)  # Output: nan
# Infinity and -Infinity Example
x = float('inf')
y = float('-inf')
print(x) # returns positive infinity (inf)
print(y) # returns negative infinity (-inf)
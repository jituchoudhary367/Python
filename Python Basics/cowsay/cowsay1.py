def odd(n):
    return n%2!=0

a = [1,3,4,6,7,8,9,56,7]
b =filter(odd,a)

print(list(b))

b = [3,5,7,8,6,9,5,3,69,9,6,9,9,25,36,15,45]
a = filter(odd,b)
print(list(a))



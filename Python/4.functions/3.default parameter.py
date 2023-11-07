# default parameters

def add_(a, b):
    return a + b

# print(add_(10, 20))

def add_(a, b, c=0):
    return a + b + c

# print(add_(10, 20))
# print(add_(10, 20, 30))


x = 10

def add_(a, b=x):       #x=10
    print(a + b)

x = 20
add_(10)
print(x)


''' if we give value to the default parameter at function call it will assign to the default parametr by overiding 
default value  or else it will take default value given at the time of defalut parametr creation'''

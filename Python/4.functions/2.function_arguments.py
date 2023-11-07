""" Positional arguments """
def greet(name, age):
    print(f"{name} is {age} years old")


# greet("Ram", 50)
# greet(50, "Ram")

""" keyword arguments """
def greet(name, age):
    print(f"{name} is {age} years old")


# greet(name="Ram", age=20)
# greet(age=20, name="Ram")

""" combination of keyword and position"""
def add_(a, b, c, d):
    print(a, b, c, d)


# add_(1, 2, 3, 4)
# add_(a=1, b=2, c=3, d=4)
# add_(1, 2, c=3, d=4)
# add_(a=1, b=2, 3, 4)    # syntax error

""" positional only arguments """
def add_(a, b, c, d, /):
    print(a, b, c, d)


# add_(1, 2, 3, 4)
# add_(a=1, b=2, c=3, d=4)  # TypeError

def add_(a, b, /, c, d):
    print(a, b, c, d)

# add_(1, 2, 3, 4)
# add_(1, 2, c=3, d=4)
# add_(a=1, b=2, c=3, d=4) # TypeError

""" keyword only arguments """

def add_(*, a, b, c, d):
    print(a, b, c, d)

# add_(a=1, b=2, c=3, d=4)
# add_(1, 2, 3, 4)      # TypeError
# add_(1, 2, c=3, d=4)  # TypeError


# def add_(a, b, *, c, d):
#     print(a, b, c, d)

# add_(1, 2, c=3, d=4)
# add_(a=1, b=2, c=3, d=4)
# add_(1, 2, 3, 4)    # TypeError


# combination of * and /

# def add_(a, b, /, *, c, d):
#     print(a, b, c, d)


# add_(1, 2, c=3, d=4)
# add_(1, 2, 3, 4)  # TypeError

""" variable positional arguments """

def spam(*args):   # packing
    print(args)


# spam(1, 2, 3)

""" sum of the arguments """

def sum_(*args):
    print(args)
    # print(sum(args))
    total = 0

    for i in args:
        if isinstance(i, (int, float)):
            total += i
    return total

# print(sum_(1, 2))

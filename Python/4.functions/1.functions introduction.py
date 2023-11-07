"""printing result in the function body"""

# def spam(val1, val2):
#     a = val1
#     b = val2
#     c = a + b
#     print(c)
#
# spam(1, 2)
# print(spam(1, 2)) # return print statement in function and as well as "spam" address also

"""returning value from the function body"""

# def spam(val1, val2):
#     a = val1
#     b = val2
#     c = a + b
#     return c
# print(spam)
# print(spam(1, 2))
# res = spam(1, 2)
# print(res)

"""returning multiple values"""

def function(a, b):
    return a, b


res = function(10, 20)
# print(res)


def f1(a):
    return "the value of a is ", a


# print(f1(56))

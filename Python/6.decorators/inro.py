# "write a decorator function that prints a messege befor the sum program"
#
# def my_deco(func):
#     def wraper(*args, **kwargs):
#         return "the sum is"
#         return func(*args, **kwargs)
#     return wraper
#
#
# @my_deco sum = my_dec(sum)
# def sum(*args, **kwargs):
#     return
#

"write decorator function that execute n times"
# import time
# def outer(n):
#     def spam(func):
#         def wraper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wraper
#     return spam # we are define one extra function that is outer after that spam function is to be executed for that
#                     # we are returning spam
# @outer(5)
# def add(a,b):
#     print(a+b)

# add(3,4)


"write decorator function that execute n times"
# def outer(n):
#     def spam(func):
#         def wraper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wraper
#     return spam # we are define one extra function that is outer after that spam function is to be executed for that
#                     # we are returning spam
# @outer(5)
# def upper(string_):
#     print(string_.upper())

# upper("kasi nadh")

"decorator function to print a messege with some dealy"
import time
# def delay(func):
#     def wraper(*args,**kwargs):
#         time.sleep(5)
#         return func(*args, **kwargs)
#     return wraper
#
# @delay #display = delay(display)
# def display(*args, **kwargs):
#     print("kasi nadh")
#     print("jmr")

# display()

"write a decorate function that prints time taken of the code"
# def outer(n):
#     def spam(func):
#         def wraper(*args, **kwargs):
#             start = time.time()
#             time.sleep(7)
#             for i in range(n):
#                 func(*args, **kwargs)
#             end=time.time()
#             print(f"ther time taken for progrsm exe is {end - start}")
#         return wraper
#     return spam
#
# @outer(3)
# def upper(string_):
#     print(string_.upper())

# upper('kasi')


"""write a decorator function to count the number of arguments passed to a function"""
# def spam(func):
#     def wraper(*args, **kwargs):
#         print(f"the no of arguments are {len(args)+len(kwargs)}")
#         return func(*args, **kwargs)
#
#     return wraper
#
# @spam
# def display(a,b,c,d):
#     pass
# display(1,2,3,d=4)

# """wap to return only positive values after substraction"""
def spam(func):
    def wraper(*args, **kwargs):

        return abs(func(*args, **kwargs))

    return wraper

@spam
def sub_(a,b):
    return a-b


sub_(-10,-5)

"""wadf to print hello world messge if the user has not given input"""
def outer_(string_ = 'hello world'):
    def spam(func):
        def wraper(*args, **kwargs):
            if string_:
                print(string_, end = ' ')
            return func(*args, **kwargs)

        return wraper

    return spam
@outer_()
def my_dis():
    print("sree")
my_dis()

"wadf that returns length of the given iterable"
def spam(func):
    def wraper(*args, **kwargs):
        return len(func(*args, **kwargs))

    return wraper

@spam
def length_(string_):
    return string_

print(length_('python'))




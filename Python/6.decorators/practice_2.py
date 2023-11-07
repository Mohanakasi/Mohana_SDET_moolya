"""examples"""
# def operators_decorator(func):
#     def operators(a,b):
#         print(a,b,sep='-')
#         print(f"the division is {a/b}")
#         print(f"the multiplication is {a*b}")
#         func(a,b)
#
#     return operators
# @operators_decorator
# def sub_add(a,b):
#     print(a,b,sep=',')
#     print(f"the addition is {a+b}")
#     print(f"the substraction is {a-b}")
#
# sub_add(20,80)




"""printing error messeges with decoraors"""
# def error_dec_div(func):
#     def wraper(a,b,flag):
#         if a>0 and b==0:
#             flag = False
#             return func(a,b,flag)
#         else:
#             return func(a,b, flag)
#     return wraper
#
# def error_eco_mul(func):
#     def wrapper(a,b,flag):
#         if a==0 or b==0:
#             flag = False
#             return func(a,b,flag)
#         else:
#             return func(a,b,flag)
#     return wrapper
# # @error_dec_div
# # def div(a,b, flag):
# #     if flag == False:
# #         return f"b non negative"
# #     return a/b
# # print(div(0,100,True))
#
# @error_eco_mul
# def mul_check(a,b,flag):
#     if flag == False:
#         return f"numbers must be greater than zero"
#     return a*b
# print(mul_check(0,10,True))


"""time decorator"""
# from time import sleep
# def delay(n):
#     def spam(func):
#         def wrapper(*args, **kwargs):
#             sleep(n)
#             print("""sorry for the delay""")
#             func(*args, **kwargs)
#         return wrapper
#     return spam
#
# @delay(4)
# def login():
#     print("welcome ti python")
#     print("start your journey in python")
#
# login()

def outer():
    def spam(func):
        def wrapper(*args, **kwargs):
            cache_ = {}
            if args in cache_:
                return cache_[args]
            cache_[args] = sum(args)
            return func(*args, **kwargs)
        return wrapper
    return spam

@outer()
def add(a,b):
    return a+b
# print(add(10,20))
# print(add(10,20))
# print(add(80,100))

"""caluculating the execution time of a function"""
from time import time
from time import sleep

def delay(n=8):
    def ex_time_deco(func):
        def wrapper(*args, **kwargs):
            start  = time()
            sleep(n)
            print(f"{func.__name__} is calling")
            func(*args, **kwargs)
            end = time()
            print(f"execution time is {end-start}")
        return wrapper
    return ex_time_deco
@delay() #prime = delay()(prime)
def prime(start, end):
    for num in range(start, end):
        for i in range(2,num):
            if num % i == 0:
                print("not a prime")
                break
        else:
            print("prime")

# prime(2,100)

"""positive decorator"""

def pos_deco(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return abs(result)

    return wrapper

@pos_deco
def sub(a,b):
    return a-b

# print(sub(104,200))

"""repeat the function n times"""
def para_rep(n):
    def repeat_n(func):
        def wrapper(*args, **kwargs):
            start = time()
            for _ in range(n):
                func(*args, **kwargs)
            end = time()
            print(f"exe time is {end-start}")
        return wrapper
    return repeat_n

@para_rep(30000)
def split_(string_):
    print(string_.split())

# split_('kasi knows python')


"""TO COUNT THE HOW MANT TIME A FUNCTION IS CALLING"""
def count_deco(func):
    func.count = 0
    # print(func.__name__,func.__dict__)
    def wrpaer(*args, **kwargs):
        func.count += 1
        result = func(*args, **kwargs)
        print(f"the function {func.__name__} is called {func.count} times")
        print(func.__name__,func.__dict__)
        return result
    return wrpaer

@count_deco
def upper(s):
    return s.upper()

# print(upper('jmr'))
# print(upper('mohana kasi'))
# print(upper('chandana'))


"""if function is called n times raise exception at nth time"""
def nth_time_break(n=8):
    def count_deco(func):
        func.count = 0
        # print(func.__name__,func.__dict__)
        def wrpaer(*args, **kwargs):
            func.count += 1
            if func.count == n:
                raise "maximum calls reached"
            result = func(*args, **kwargs)
            print(f"the function {func.__name__} is called {func.count} times")
            # print(func.__name__,func.__dict__)
            return result
        return wrpaer
    return count_deco

@nth_time_break()
def upper(s):
    return s.upper()

# print(upper('jmr'))
# print(upper('mohana kasi'))
# print(upper('mohana kasi'))
# print(upper('mohana kasi'))
# print(upper('mohana kasi'))
# print(upper('mohana kasi'))
# print(upper('mohana kasi'))
# print(upper('mohana kasi'))
# print(upper('mohana kasi'))
# print(upper('mohana kasi'))

"""write a decorator function that return how many arguments passed to a main function"""
def arg_count_deco(func):
    def wrapper(*args, **kwargs):
        print(f"the total arguments passed is {len(args)+len(kwargs)}")
        func(*args, **kwargs)

    return wrapper

@arg_count_deco
def dictionary_traver(**kwargs):
    for key in kwargs:
        if isinstance(kwargs[key], str):
            print(kwargs[key][::-1])

dictionary_traver(a=100,b='jmr',c='kasi', d={1,2,32})

# "simple decorate function"
# import time
# # def delay(func):
# #     def wraper(*args, **kwargs):
# #         time.sleep(5)
# #         return func(*args, **kwargs)
# #     return wraper
# #
# # @delay
# # def add(a,b):
# #     return a+b    qas
# #
# # print(add(1,2))
#
# "write a decorator function to reverse a string with 5 seconds delay"
# # def delay_string(func):
# #     def wraper(*args, **kwargs):
# #         time.sleep(5)
# #         return func(*args, **kwargs) #in wrper function we are binding extra functionality and main function calling
# #     return wraper
# #
# # @delay_string # string_rev = delay_string(string_rev)
# # def string_rev(string_):
# #     return string_[::-1]
# #
# # print(string_rev('kasi'))
#
# "welcome example"
# # def welcome(func):
# #     def wraper(*args, **kwargs):
# #         print(f"welcome to {func.__name__}")
# #         return func(*args, **kwargs)
# #     return wraper
# #
# # @welcome
# # def greeting():
# #     return "hi kasi"
# #
# # print(greeting())
# #
# # @welcome
# # def sales():
# #     return "sales"
# #
# # print(sales())
# #
# # @welcome
# # def loans():
# #     return "loans page"
# #
# # print(loans())
#
# "reverse a stirng decorator"
# def rev_string(func):
#     def wraper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         if isinstance(res, str):
#             return res[::-1]
#         return res
#     return wraper
#
# @rev_string
# def data(name):
#     return name
#
# print(data("kasi"))
#
# @rev_string
# def age(name):
#     return  name
#
# print(age(789))
#
# ""
# import time
# # def ex_time(func):
# #     def wraper(*args, **kwargs):
# #         start = time.time()
# #         res = func(*args, **kwargs)
# #         end = time.time()
# #         print(f"the execution time of {func.__name__} is {end-start} seconds")
# #         return res
# #     return wraper
# #
# # @ex_time
# # def add(a,b):
# #     time.sleep(10)
# #     return a + b
# #
# # print(add(10,80))
# #
# # @ex_time
# # def rev_string(string_):
# #     time.sleep(5)
# #     return string_[::-1]
# #
# # print(rev_string('mohana'))
#
# "count of the functions by using decorators"
# from collections import defaultdict
# _count = defaultdict(int)
# # def func_count(func):
# #     def wraper(*args, **kwargs):
# #         _count[func.__name__] += 1
# #         return func(*args, **kwargs)
# #     return wraper
# #
# # @func_count
# # def string_rev(string_):
# #     return string_[::-1]
# #
# # print(string_rev('kasi'))
# #
# # print(_count)
# #
# # print(string_rev('kasi'))
#
# "using function attribute creation"
# # def func_count(func):
# #     func.count = 0
# #     def wraper(*args, **kwargs):
# #         func.count += 1
# #         result = func(*args, **kwargs)
# #         print(f"the function {func.__name__} is called {func.count} times")
# #         return result
# #     return wraper
# #
# # @func_count
# # def string_rev(string_):
# #     return string_[::-1]
# #
# # print(string_rev('kasi'))
#
# "count the function and if count reached more than 5times raise value error"
# # def func_count(func):
# #     func.count = 0
# #     def wraper(*args, **kwargs):
# #         func.count += 1
# #         if func.count > 5:
# #             raise ValueError(f"the maximum calls to function {func.__name__} is exceeded")
# #         return func(*args, **kwargs)
# #     return wraper
# #
# # @func_count
# # def string_rev(string_):
# #     return string_[::-1]
# #
# # print(string_rev('kasi'))
# # print(string_rev('mohana'))
# # print(string_rev('rao'))
# # print(string_rev('err'))
# # print(string_rev('poo'))
# # print(string_rev('kasi'))
#
#
# ""
# def func_count(func): #func = string_rev
#     func.count = 0
#     def wraper(*args, **kwargs):
#         for _ in range(10):
#             func.count += 1
#             if func.count > 10:
#                 raise ValueError(f"the maximum to function {func.__name__} is exceeded")
#             result = func(*args, **kwargs)
#         return result
#     return wraper
#
# @func_count #string_rev = func_count(string_rev)
# def string_rev(string_)
#     return string_[::-1]
#
# # print(string_rev('kasi'))
#
# ""
# # def cache(func):
# #     func._cache = {}
# #     def wraper(*args, **kwargs):
# #         if args in func._cache:
# #             print(f"getting result from cache")
# #             return func._cache[args]
# #         print("excecuting for the first time")
# #         result = func(*args, **kwargs)
# #         func._cache[args] = result
# #         return result
# #     return wraper
# #
# # @cache
# # def add(a,b):
# #     time.sleep(5)
# #     return a+b
# #
# # print(add(1,2))
# # print(add(1,2))
#
#
# ""
# # list_ = [8886213059,919491294540]
# # for index,item in enumerate(list_):
# #     if len(str(item)) == 10:
# #         list_[index] = '+91-'+str(item)
# #     elif len(str(item)) == 12 and str(item)[:2] == '91':
# #         list_[index]= '+'+str(item)[:2]+'-'+str(item)[2:]
# # print(list_)
#
#
# # def prefix(number):
# #     str_num = str(number)
# #     if len(str_num) == 10:
# #         return "+91"+str_num
#
#
# ""
# # def validate_(*expected_types):
# #     def spam_(func):
# #         def wraper(*args, **kwargs):
# #             for actual_value,expected_type in zip(args,expected_types): #args = [1,2],(1,2) (int,int)
# #                 if not isinstance(actual_value, expected_type):
# #                     raise TypeError()
# #             return func(*args, **kwargs)
# #         return wraper
# #     return spam_
# #
# # @validate_(int, int) #  add = spam_(add)
# # def add(a, b):
# #     return a+b
#
# # print(add(1,2))
#
# # def spam_(func):
# #     def wraper(*args, **kwargs):
# #         for item in args:
# #             if not isinstance(item, int):
# #                 raise TypeError()
# #         return func(*args, **kwargs)
# #     return wraper
# #
# # @spam_ add = spam_(add)
# # def add(a, b):
# #     return a+b
# #
# # print(add(1,2))
#
# # "adding atribute in main function using decorator"
# #
# # def attach_(func):
# #     func.count = 0
# #     return func
# #
# # @attach_
#
#
#
# #clousere function
# # a.__clouser__ # to know the clousere variables
#
# # def add(a,b):
# #     name = 'kasi'  # name, a, b are clousere variables
# #     def wraper():
# #         print(name)
# #         return a+b
# #     return wraper
# #
# # a = add(1,2)
# # print(a())
# "a function is called as a varibale or parameter in another fuynction tht fnction is called as callback function"
# # import time
# # def add(a,b):
# #     name = 'kasi'  # name, a, b are clousere variables
# #     def wraper():
# #         print(name)
# #         return a+b
# #     return wraper
# #
# # def delay(seconds, func):
# #     time.sleep(seconds)
# #     return func()
# #
# # a = add(1,2) # contains wraper function addfress
# # print(delay(5,a)) # giving 5seconds and wraper func address to delay as arguments
#

# "documentaion string"
# # def add(a,b):
# #     name = 'kasi'  # name, a, b are clousere variables
# #     def wraper():
# #         print(name)
# #         return a+b
# #     return wraper
# #
# # def delay(seconds, func):
# #
# #     time.sleep(seconds)
# #     return func()
# # a = add(1,2) # contains wraper function addfress
# # print(delay(5,a))

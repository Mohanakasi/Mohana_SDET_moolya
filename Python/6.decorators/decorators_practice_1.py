""""log decorator"""

# def log_(msg = 'hello there'):
#     def samp(func):
#         def wrapper(*args, **kwargs):
#             print(f"{msg} welcome to bmw showroom")
#             return func(*args, **kwargs)
#         return wrapper
#     return samp
#
# @log_()
# def split_(model_, cost):
#     return model_, cost
#
# print(split_('bmw89',89000000))
#

# """delay decorator"""
# import time
# def delay(n_sec):
#     def spam(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(n_sec)
#             print(f"welcome to {func.__name__}")
#             func(*args, **kwargs)
#
#         return wrapper
#     return spam
#
# @delay(5)
# def hdfc_bank(name, balance):
#     print(f"account holder name: {name}")
#     print(f"account balance:{balance}")
#
# hdfc_bank('kasi',-320)


"""write a decorator program that reverse a string if the main funcion return type is string else raise error"""
# def rev_string_(func):
#     def wraper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, str):
#             return result[::-1]
#         else:
#             raise "enter only strings"
#     return wraper
#
# @rev_string_
# def data_type_check(data):
#     return data
#
# print(data_type_check('python oops'))



"""caluculating excecution time of a function using decorator"""
# from collections import defaultdict
# import time
# def exe_time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         print(func(*args, **kwargs))
#         end = time.time()
#         return f"eecution time of the function is {end-start}"
#     return wrapper
#
# @exe_time
# def word_count_pair(string_):
#     d = defaultdict(int)
#     words = string_.split()
#     for word in words:
#         # d[word] = words.count(word) # using inbuilt method
#         d[word] += 1 # without inbuilt
#     return d
# print(word_count_pair('kasi is from guntur kasi knows python guntur'))



"""write a decorator checks the main function output if it is negative convert it to posiive else return as it is"""
# def positive_(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if result < 0:
#             return abs(result)
#         else:
#             return result
#     return wrapper
# @positive_
# def sum(a,b):
#     return a-b
#
# print(sum(50,80))
#

"""repeat a function for n times using deorator"""
# def rep_func(n):
#     def spam(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 print(func(*args, **kwargs))
#         return wrapper
#     return spam
#
# @rep_func(5)
# def company_(string_):
#     return string_.upper()
#
# company_('i am in Bangalore')

"""counting no of function calls of a function"""
# def count_(func):
#     func.count = 0
#     def wrapper(*args, **kwargs):
#         func.count += 1
#         func(*args, **kwargs)
#         return f"the function {func.__name__} is called {func.count} times"
#     return wrapper
#
# @count_
# def revers_(string_):
#     print(string_[::-1])
#
# print(revers_('kasi'))
# print(revers_('mohana'))
# print(revers_('jmr'))
# print(revers_('python language'))



"""write a decorator that prfix the +91 before the number"""
# def country_code(code = "+91", sym = "+"):
#     def ph_num(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             if len(result) == 10:
#                 result = code + result
#                 return result
#             elif len(result) == 12 or result[0:2] == '91':
#                 result = sym+result
#                 return result
#             elif result[0:3] == code:
#                 return result
#             else:
#                 raise "invalid number"
#         return wrapper
#     return ph_num
# @country_code()
# def mobile_num(number):
#     return number
#
# print(mobile_num('+918886213059'))


# import time
# def outer(func):
#     def wraper(*args, **kwargs):
#         time.sleep(5)
#         return func(*args, **kwargs)
#     return wraper
#
# @outer # add = outer(add) # wraper
# def add(a,b):
#     return a+b
# print(add(10,20))
#
# # @outer
# # def sub(a,b):
# #     return a-b
# # print(sub(50,80))


# def n_time(n):
#     def spam(func):
#         def wraper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wraper
#     return spam
#
# @n_time(5)
# def rev(string_):
#     print(string_[::-1])
#
# rev('kasi')

# def count_func(func):
#     func.count = 0
#     def wraper(*args, **kwargs):
#         func.count += 1
#         result = func(*args, **kwargs)
#         print(f"the {func.__name__} is excecuted {func.count} time")
#         return result
#     return wraper
#
# @count_func
# def upper(string_):
#     return string_[::-1]
# print(upper('python is a language'))
# print(upper('kasi'))


"count the function how many times it is called and raise value error if it is called more than 5 times"
# def count_(func):
#     func.count = 0
#     def wraper(*args, **kwargs):
#         func.count += 1
#         result = func(*args, **kwargs)
#         if func.count >=5:
#             raise ValueError(f"the {func.__name__} is exceeded {func.count} times")
#         print(result)
#         return result
#
#     return wraper
#
# @count_
# def rev(string_):
#     return string_[::-1]
#
# print(rev('kasi'))
# print(rev('rao'))
# print(rev('ertop'))
# print(rev('oper'))
# print(rev('king'))
# print(rev('out'))



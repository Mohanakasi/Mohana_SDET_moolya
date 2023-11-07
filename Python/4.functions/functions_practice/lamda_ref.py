'"""lambda expression for print las element of a equence"""'''
# res = lambda sequence: sequence[-1]
# print(res('kasi'))

"""write a lambda function that checks if the string is palindrome or not"""
# res = lambda string: string == string[::-1]
# print(res('mom'))

"""lambda expression to check string is a palindrome and to print it if it is a palindrome"""
# res = lambda string: string if string == string[::-1] else none
# print(res('mom')) #'''single if not possible in lambda expressions  '''


"""wap that checks whether the no is even or odd print the no in both the cases"""

# res = lambda num: 'even' if num % 2 == 0 else 'odd'
# print(res(0))

# """lambda expression to check string is of even length and string stars with vowel0"""
sequence = 'Iamkasij'
even = lambda s: s if len(s) % 2 == 0 and s[0].lower() in 'aeiou' else None
print(even(sequence))

"""to check the numbers present inside the list are even or off"""
# list_ = [1,2,108,320,580]
# res = lambda num: f"{num} is even" if num % 2 == 0 else f"{num} is odd"
# print(list(map(res,list_)))

# def ev_odd(num):
#     if num % 2 == 0:
#         return f"{num} is even"
#     return f"{num} is odd"


"""wap to return the string which are starting wit vowels"""
# list_ = ['i am kasi','mom','ur']
# def myfunc(string_):
#     if string_[0].lower() in 'aeiou':
#         return string_
# res = map(myfunc, list_) # it will return none if condition false
# print(list(res))

# res = filter(myfunc, list_)
# print(list(res))



#assignment
# wap to convert all the strings in the list to upper case using map
# wap to convert allthe negeative numbers into positive using map
# wap that returns the list of numbers raised to the power of their indices using map
# wap that returns all the words in lower case in the given sentence

import os
path = r"C:\Users\Hp\PycharmProjects\python_training\file handling\sample.txt"
with open(path) as f1:
    print(f1.read())
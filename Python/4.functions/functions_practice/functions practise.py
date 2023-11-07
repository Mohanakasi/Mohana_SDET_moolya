# '''printing a series of  numbers using functions '''
# def numbers(start, end, sv = 1):
#     for num in range(start, end, sv):
#         print(num, end = ' ')
#
#
# numbers(1, 11)
# print()
# '''printing 10 to 1 '''
# numbers(10, 0, -1)
# print()
# '''printing -1 to -10'''
# numbers(-1, -11, -1)
# '''printing -10 to -1'''
# print()
# numbers(-10, 0, 1)
#
# '''printing a series of numbers using function by list comprehension'''
# def numbers(start, end, sv = 1):
#     res = [num for num in range(start, end, sv)]
#     return res
#
#
# print(numbers(1, 11))
# print()
# '''printing 10 to 1 '''
# print(numbers(10, 0, -1))
# print()
# '''printing -1 to -10'''
# print(numbers(-1, -11, -1))
# '''printing -10 to -1'''
# print()
# print(numbers(-10, 0, 1))
#
# print()
# print()
# '''printing a series of numbers using function by set comprehension'''
# def numbers(start, end, sv = 1):
#     res = {num for num in range(start, end, sv)}
#     return res
#
#
# print(numbers(1, 11))
# print()
# '''printing 10 to 1 '''
# print(numbers(10, 0, -1))
# print()
# '''printing -1 to -10'''
# print(numbers(-1, -11, -1))
# '''printing -10 to -1'''
# print()
# print(numbers(-10, 0, 1))
#
#

# '''even no's from 1 to 10'''
# def even(start, end):
#     for num in range(start, end):
#         if num % 2 == 0:
#             print(num,end = ' ')
#
#
# even(1,10)
# print()
# even(50,100)
# print()
# even(abs(-150),abs(-200))

#
# # '''traversing through iterables'''
# def traverse(iterable):
#     if isinstance(iterable,(str,tuple,list,set)):
#         for value in iterable:
#             print(value, end=' ')
#     elif isinstance(iterable,dict):
#         for key in iterable:
#             print(key,"---->",iterable[key])
#
#
# traverse('kasi is a king')
# print()
# '''list traverse'''
# traverse([1,2,3,'kasi',['jmr']])
# print()
# ''' tuple traverse'''
# traverse((1008,'kasi','jmr',{4568}))
# print()
# '''set traverse'''
# traverse({'hai','hello','kasi','ela','unnav'})
# print()
# print("********************")
# print("dictionary traverse")
# traverse({'kasi':1995, 'jmr':1995, 'met': 2020})
#


'''to print index and item in iterables'''
# def func(iterable):
#     if isinstance(iterable, (str, tuple, list, set)):
#         for index,item in enumerate(iterable):
#             print(index, "------>",item)
#     elif isinstance(iterable,dict):
#         for index,(key,value) in enumerate(iterable.items()):
#             print(index,"---->",key,"----->",value)
# #
#
# func('python')
# print()
# '''for list'''
# func([1,1008,True,'kasi'])
# '''for tuple'''
# func((1,2,3,[8569,'kasi']))
# print()
# ''' for set'''
# func({1,2,23,True,'kasi'})
# print("dictionary")
# func({'kasi': 1995, 'jmr': 1995, 'met': 2020})

# '''traversing through iterables in reverse order'''
# def traverse(iterable):
#     if isinstance(iterable,(str, tuple, list)):
#         for item in reversed(iterable):
#             print(item,end=' ')
#     elif isinstance(iterable,dict):
#         list_ = list(iterable)
#         for key in reversed(list_):
#             print(key, ":", iterable[key], end = ' ')
#     elif isinstance(iterable,(set,int,float,bool,complex)):
#         print(f"reverse traversing not possible in {iterable} as unavailable of index")
#
#
# traverse('python')
# print()
# '''for list'''
# traverse([1,1008,True,'kasi'])
# '''for tuple'''
# traverse((1,2,3,[8569,'kasi']))
# print()
# ''' for set'''
# traverse({1,2,23,True,'kasi'})
# print("dictionary")
# traverse({'kasi': 1995, 'jmr': 1995, 'met': 2020})

# '''counting no of characters or items in a iterable'''
# def count(iterable):
#     count = 0
#     for _ in iterable:
#         count += 1
#     return f"the iterable consist of {count} items"
#
#
# print(count('kasi knows python'))
# print(count([1, 2, 3, 'kasi', 'jmr']))
# print(count(('kasi python', 1, 2, True, [1008,'python'])))
# print(count({'hello','jmr','how','are','you',10008}))
# print(count({'a':1, 'b':250, 'c':330, 'd':8010}))


# '''counting even indexed items in ierable'''
# def count(iterable):
#     count = 0
#     if isinstance(iterable,(str, list, tuple)):
#         for index,item in enumerate(iterable):
#             if index % 2 == 0:
#                 count += 1
#         return f"the iterable has {count} even index items"
#     elif isinstance(iterable, (set, dict, int, float, complex, bool)):
#         return f"countong of even index items not possible as {type(iterable)} has no indexing"
#
#
# print(count('kasi knows python'))
# print(count([1, 2, 3, 'kasi', 'jmr']))
# print(count(('kasi python', 1, 2, True, [1008,'python'])))
# print(count({'hello','jmr','how','are','you',10008}))
# print(count({'a':1, 'b':250, 'c':330, 'd':8010}))

# '''print the digits in the iterable'''
# def traverse(iterable):
#     if isinstance(iterable, (tuple,set,list)):
#         for item in iterable:
#             if isinstance(item, int):
#                 print(item, end = ' ')
#     elif isinstance(iterable, str):
#         for char in iterable:
#             if char.isdigit():
#                 print(char, end = ' ')
#     elif isinstance(iterable, dict):
#         for key in iterable:
#             if isinstance(iterable[key], int):
#                 print(iterable[key], end = ' ')
# traverse('hello 1008 python 3.10.1')
# print()
# traverse([1, 2, 3, 'kasi', 'jmr'])
# print()
# traverse(('kasi python', 1, 2, True ,1008,100000,[1008,'python']))
# print()
# traverse({'hello','jmr','how','are','you',1995,2020})
# print()
# traverse({'a':1, 'b':250, 'f': 'kasi', 'c':330, 'd':8010})

# '''print the no of small letters and no of capital letters in a string'''
# def count(string_):
#     small = 0
#     caps = 0
#     for char in string_:
#         if char.isupper():
#             caps += 1
#         elif char.islower():
#             small += 1
#     print(f"the string has {small} small letters")
#     print(f"the string has {caps} capital letters")
#
#
# count('Hello KASI is IN BANGALORE')
# print()
# count('hello PYTHON')
# print()
# count('BANGALORE Is A Big City')


# '''print lenth of the each string present inside the list, tuple, set, and dictionary '''
# def length(iterable):
#     if isinstance(iterable, (list, tuple, set)):
#         for item in iterable:
#             if isinstance(item, str):
#                 print(f"the legth of the string {item} is {len(item)}")
#     elif isinstance(iterable, dict):
#         for key in iterable:
#             if isinstance(iterable[key], str):
#                 print(f"the legth of the string {iterable[key]} is {len(iterable[key])}")
#     elif isinstance(iterable, str):
#         print("please give iterables other than string")
#     else:
#         print("the input given is not a iterable")
#
# print("list")
# length([10008, 'kasi', 'jmr', True, 50+50j, ['hai', 'hello', 'how']])
# print("******************************")
# print('dictionary')
# length({'a': 'kasi nadh', 'b': 'jaya madhuri', 'c': 10008, 'd': True, 'f': [0,1,20]})
# print("******************************")
# print("tuple")
# length((1, 2, 3, 'python', 'kasirobo', 'bangalore', ['moto'], 'chennai'))
# print("******************************")
# print("set")
# length({4589, 'madiwala', ' sandha', 'hotel jmr', 50+50j, True, 1.58669})
# print("******************************")
# print('dictionary')
# length({'a': 'kasi nadh', 'b': 'jaya madhuri', 'c': 10008, 'd': True, 'f': [0,1,20]})
# print()
# length("hello world")
# length(1.586)

# '''print only numeric data present  inside the list, tuple, set, and dictionary '''
# def length(iterable):
#     if isinstance(iterable, (list, tuple, set)):
#         for item in iterable:
#             if isinstance(item, (int,float,complex)):
#                 print(item, end = ' ')
#     elif isinstance(iterable, dict):
#         for key in iterable:
#             if isinstance(iterable[key], (int,float,complex)):
#                 print(iterable[key], end = ' ')
#     elif isinstance(iterable, str):
#         print("please give iterables other than string")
#     else:
#         print("the input given is not a iterable")
#
# print("list")
# length([10008, 'kasi', 'jmr', True, 50+50j, ['hai', 'hello', 'how']])
# print()
# print("******************************")
# print('dictionary')
# length({'a': 'kasi nadh', 'b': 'jaya madhuri', 'c': 10008, 'd': True, 'f': [0,1,20]})
# print()
# print("******************************")
# print("tuple")
# length((1, 2, 3, 'python', 'kasirobo', 'bangalore', ['moto'], 'chennai'))
# print()
# print("******************************")
# print("set")
# length({4589, 'madiwala', ' sandha', 'hotel jmr', 50+50j, True, 1.58669})
# print()
# print("******************************")
# print('dictionary')
# length({'a': 'kasi nadh', 'b': 'jaya madhuri', 'c': 10008, 'd': True, 'f': [0,1,20]})
# print()
# length("hello world")
# length(1.586)


# '''print the strings having even lenth present inside a list'''
# l = ['kasi', 2020, 'jaya madhuri', 'guntur', 2020]
# def eve_len(*args):
#     for item in args:
#         if isinstance(item, str) and len(item) % 2 == 0:
#             print(item, end = ' ')
#
# eve_len(*l)

# '''reverse the string elemts else keep it as it is in side the list'''
# l = ['kasi', 2020, 'jaya madhuri', 'guntur', 2020]
# def func(*args):
#     list_ = []
#     for item in args:
#         if isinstance(item, str):
#             list_.append(item[::-1])
#         else:
#             list_.append(item)
#     return list_
#
#
# print(func(*l))

# '''printing strings starting with vowel present inside a dictionary'''
# def vow_check(**kwargs):
#     for key in kwargs:
#         if isinstance(kwargs[key], str) and kwargs[key][0].lower() in 'aeiou':
#             print(kwargs[key])
#
#
# vow_check(a='kasi', b=1008, c='jmr', d ='IAM in BANgalore', e='unstoppable')

# '''printing strings starting with vowel present inside a dictionary'''
# def vow_check(**kwargs):
#     for value in kwargs.values():
#         if isinstance(value, str) and value[0].lower() in 'aeiou':
#             print(value)
#
# print("*******************")
# print("using values inbuilt method")
# print("*************************")
# vow_check(a='kasi', b=1008, c='jmr', d = 'IAM in BANgalore', e='unstoppable')

# '''printing all the extensions of strings present inside a list as keys into the dictionary and
# file names as values'''
# l = ['gmail.exe','youtube.pdf','kasi_ressume.pdf','apple.exe','facebook.txt']
# def file_exte(*args):
#     from collections import defaultdict
#     d = defaultdict(list)
#     for item in args:
#         list_ = item.split('.')
#         d[list_[-1]] += [list_[0]]
#
#     return d
#
# print(file_exte(*l))

# '''printing all the extensions of strings present inside a list as keys into the dictionary and
# file names as values if file name has odd length'''
# l = ['gmail.exe','youtube.pdf','kasi_ressume.pdf','apple.exe','facebook.txt']
# def file_exte(*args):
#     from collections import defaultdict
#     d = defaultdict(list)
#     for item in args:
#         list_ = item.split('.')
#         if len(list_[0]) % 2 != 0:
#             d[list_[-1]] += [list_[0]]
#
#     return d
#
# print(file_exte(*l))

# '''index of the first occurence of a given element present inside a colllection'''
# def func(num,*args):
#     for index,item in enumerate(args):
#         if item == num:
#             print(f"thhe index of the element '{num}' is {index}")
#             break
#     else:
#         print("the element not found inthe list")
#
#
# func(50000,2,3,4,5,6,8,'kasi','jmr',2020,1008,'bangalore')


# '''checking a nu,ber is a prime number or not'''
# def prime(num):
#     for i in range(2,num):
#         if num % i == 0:
#             print(f"'{num}' not a prime number")
#             break
#     else:
#         print(f"'{num}' is a prime number ")
#
#
# prime(7)


'''checking the numbers present inside the list prime or not'''

# def prime_series(*args):
#     print(args)
#     for item in args:
#         for i in range(2,item):
#             if item % i == 0:
#                 print(f" '{item}' is not a prime number")
#                 break
#         else:
#             print(f"'{item}'  is a prime number")
#
#
# print(prime_series(1,2,7,27,100,101,103,156))


# '''checking a number is a fibonaci no or not'''
# def fibo(num):
#     first = 0
#     second = 1
#     while first <= num:
#         if first == num:
#             print(f"the '{num}' is a fibonaci number")
#             break
#         else:
#             c = first+second
#             first = second
#             second  = c
#     else:
#         print(f" the '{num}'  is not a fibonaci number")
# fibo(89)

# '''generating nth fibonaci numbers'''
#
# def nth_fibo_nos(n):
#     first = 0
#     second = 1
#     i = 1
#     while i<=n:
#         print(first)
#         c = first + second
#         first = second
#         second = c
#         i += 1
#
# nth_fibo_nos(10)

# '''checking a series of numbers in a list are prime or not'''
#
# def fibo_series(*args):
#     for num in args:
#         first = 0
#         second = 1
#         while first<=num:
#             if first == num:
#                 print(f"thhe '{num}' is a fibonaci number")
#                 break
#             else:
#                 c =first + second
#                 first = second
#                 second = c
#         else:
#             print(f"'{num} is not a fibonaci number'")
#
# fibo_series(0,1,6,4,2,25,75,89,55)

# ''' generate fibonaci numbers for a particular range'''
#
# def fibo_nos(end, start = 0):
#     first = 0
#     second = 1
#     i = 1
#     while first <= end:
#         if start <= first <= end:
#             print(first, end = ' ')
#         c = first + second
#         first = second
#         second = c
# fibo_nos(10)

# l = [1,2,3,4]
# res  = lambda num: num[2] % 2 == 0
# print(res(l))


# res = map(lambda x: x%2 == 0, [1,2,3,4])
# print(list(res))

# a = map(lambda x: x% 2 == 0, b)
# print(a(10))
#
# a = lambda x: x*2
# print(a((1,2)))

# a = lambda x,y: x*2, y+3
# """lambda has collection as argument but we cant iterate it """


"""even numbers"""
# def ev(end, start = 0):
#     list_ = []
#     for num in range(start, end+1):
#         if num % 2 == 0:
#             list_.append(num)
#     return list_
#
# print(ev(50))

""""prime numbers"""
# def prime(end, start=2):
#     res = []
#     for num in range(start, end):
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#         else:
#             res.append(num)
#     return res
#
# print(prime(20))


"""fibonaci series"""
# def fibo(n):
#     first = 0
#     second = 1
#     i = 0
#     while i < n:
#         c = first +second
#         print(first)
#         first = second
#         second = c
#         i += 1
#
# fibo(10)

#
# """checking a number is a fibo number or not"""
# def fibo(num):
#     first = 0
#     second = 1
#     while first<=num: # when we want to find a number is a fibo number or not
#         if num == first:
#             return f"the {num} is a fibonaci no"
#             break
#         else:
#             c = first + second
#             first = second
#             second = c
#     return f"the {num} is not a fibo number"
#
# print(fibo(3))



num  = 12
def prime(num):
    number = num
    while number > 0:
        for i in range(2,number):
            if number % i == 0:
                flag = False
            elif flag == True:
                print(f"the given {number} is a prime number")
            else:
                number += 1
        else:
            print(number)
            return "the next number is prime"
        break
print(prime(12))


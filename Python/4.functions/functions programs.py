'''printing the even numbers from 1 to 50 '''
# def even(a,b):
#     for item in range(a,b):
#         if item % 2 == 0:
#             print(item,end=' ')
# even(1,50)

''' printing a list of even numbers from 1 to 50 using return statement'''
# def even(a,b):
#     list_ = []
#     for item in range(a,b):
#         if item % 2 == 0:
#             list_.append(item)
#     return list_
# print(even(1,50))
#
# def even(end, start = 1): '''default parameter must be present after the actual parameter '''
#     list_ = []
#     for item in range(start,end):
#         if item % 2 == 0:
#             list_.append(item)
#     return list_
# print(even(50))

''' if we give value to the default parameter at function call it will assign to the default parametr by overiding 
default value  or else it will take default value given at the time of defalut parametr creation'''

#
# '''variable positional arguments (pACKING)'''
# def sum_(*args):
#     sum2_ = 0
#     for item in args:
#         sum2_ += item
#     return sum2_
# print(sum_(1,2,32,5.5))
#
# '''variable positional arguments (pACKING)'''
# def sum_(*args):
#     print(sum(args))
# sum_(1,2,32,5.5)
#
# #
# # # returniung no of positional arguments passed in function call
# # def temp(*args):
# #     return len(args)
# # print(temp(1,2))
# #
# #
# # def temp(*args):
# #     count = 0
# #     for _ in args:
# #         count += 1
# #     return count
# # print(temp(1,2,8,8,10))

# printing integers only when variable positonal argms passed
# def vpos(*args):
#     for item in args:
#         if isinstance(item,int):
#             print(item) # here we cant take return sttement
# vpos(1,2,3,4.5,'kasi',50+50j)

''' if string passed as positional arguments reverse it'''
# def margs(*args):
#     list_ = []
#     for item in args:
#         if isinstance(item,str):
#             list_.append(item[::-1])
#     print(list_)
# margs(1,2,3,4.5,'kasi','jmr')
#
# def margs(*args):
#     list_ = []
#     for item in args:
#         if isinstance(item,str):
#             list_.append(item[::-1])
#
#         else:
#             list_.append(item)
#     print(list_)
# margs(1,2,3,4.5,'kasi','jmr')
#
# l = [1,2,3]
# def unpack(*args):
#     return args[0],args[1],args[2]
# print(unpack(*l))
#
# def temp():
#     return 'hai   '
# print(temp())
#
# def prime(num):
#     for item in range(2,num):
#         if num % item == 0:
#             print("not a prime")
#             break
#     else:
#         print("prime")
# prime(11)
#
# def temp(num):
#     return int(str(num)[-1])
# print(temp(1008))


# def tail(sequence,n):
#     return sequence[-n:]
# print(tail('python is a progrmaiing',8))

# # to check perfect square or not
# def isperfectsquare(num):
#     for i in range(num):
#         if i*2 == num:
#             return True
#     return False
# print(isperfectsquare())

# # to check if the given no is fibo no or not
# def fibo(n):
#     a = 0
#     b = 1
#     while a<=n:
#         if a == n:
#             return f'{n} is a fibo no'
#             break
#         c = a+b
#         a = b
#         b = c
#     return f'{n} is  not a fibo'
# print(fibo(0))

# def length_(**kwargs):
#     print(kwargs)
#     for key in kwargs:
#         if isinstance(kwargs[key],(str,list,tuple,set,dict)):
#             print(kwargs[key],'.....>',len(kwargs[key]))
# length_(a='kasi',b=100,c='jmr',d=[1,2,3])


# def count_string(string_):
#     d = {}
#     for char in string_:
#         d[char] = string_.count(char)
#     return d


# print(count_string('hai hello python'))

# def count_string(string_):
#     d = {}
#     for char in string_:
#         if char not in d:
#             d[char] = 1
#         else:
#             d[char] += 1
#     return d
#
# print(count_string('hello kasi'))
#
#
# def count_string(string_):
#     from collections import defaultdict
#     d = defaultdict(int)
#     for char  in string_:
#         d[char] += 1
#     return d
#
#
# print(count_string('hello kasi'))


# to print a series of numbers using recursion
# def count(n):
#     if n <= 10:
#         print(n)
#         n +=1
#         count(n)
#     else:
#         return
#
# count(1)

# to print a series of numbers using recursion
# def count(n):
#     if n > 10:
#         return
#     print(n)
#     count(n+1)
#
#
# count(1)
#


# to print a range of numbers using recursion
# def count(start, end):
#     if start > end:
#         return
#     print(start)
#     count(start+1, end)
#
#
# count(1, 10)


# to print 10 to 1 using recursion
# def count(start, end):
#     if start < end:
#         return
#     print(start)
#     count(start-1, end)
#
#
# count(10, 1)

# num = 123
# temp = num
# sum = 0
# while temp>0:
#     last = temp%10
#     sum += last
#     temp = temp//10
# print(sum)
#
# def add(num, sum = 0):
#     if num>0:
#         last = num % 10
#         print(sum)
#         sum += last
#         print(sum)
#         num = num//10
#         add(num, sum)
#
#
#
# print(add(123))+3

#
# def sum_(num, sum = 0):
#     if num > 0:
#         sum += num
#         return sum_(num-1, sum)
#     return sum
# print(sum_(5))

#write a recursion program to find the factorial of a number
# def facto(num, fac = 1):
#     if num > 0:
#         fac *= num
#         return facto(num-1, fac)
#     return fac
#
#
# print(facto(5))


# def temp(num, count = 0):
#     if num > 0:
#         count += 1
#         num = num//10
#         return temp(num, count)
#     return count
#
# print(temp(3456))

# # to reverse the string using recursion
# def reverse(string_, res = ' ', index = 0):
#     if index < len(string_):
#         res = string_[index] + res
#         return reverse(string_, res, index+1)
#     return res
#
# print(reverse('hai'))

# w a r p to print fibonaci series upto n


# def fibo_series(n, first = 0, second = 1, count = 0):
#     count += 1
#     if count < n and first < 1000:
#         print(first)
#         c = first + second
#         first = second
#         second = c
#         return fibo_series(n, first, second, count)
#     print(first)
#
#
# fibo_series(20)

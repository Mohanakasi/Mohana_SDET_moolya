class my_class:
    trainer = 'kasi'
    salary = 15000
    def __init__(self, a, b):
        self.a = a
        self.b = b
    @classmethod
    def change_(cls):
        cls.trainer = 'mohana kasi'
        cls.salary = 16000
    @staticmethod
    def temp(s,l):
        return len(s)+len(l)

# a1 = my_class(10,20)
# print(my_class.temp('kasi','s'))


class eve_odd:

    def __call__(self,num):
        if num % 2 == 0:
            print("even")
        else:
            print("odd")

# a1 = eve_odd()
#
# a1(208)

# class log:
#     def __call__(self,func):
#         def wrapper(*args, **kwargs):
#             func(*args, **kwargs)
#             print("hai")
#         return wrapper
#
# @log()
# def add(a,b):
#     print(a+b)
# add(20,20)


"""class decorator to sleep a function for n seconds"""
from time import sleep
class func_sleep:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            sleep(5)
            return func(*args, **kwargs)

        return wrapper

@func_sleep()
def add(a,b):
    return a+b

# print(add(40,80))

"""example"""
class temp:
    def __init__(self,n):
        self.n = n

# print(temp(10).__dict__)

"""using parametraised class decorator"""
from time import sleep
class func_sleep:
    def __init__(self, n):
        self.n = n
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            sleep(self.n)
            return func(*args, **kwargs)

        return wrapper

@func_sleep(5)
def add(a,b):
    return a+b

# print(add(40,80))


"""write a parametraised class decorator to execute a function for n times"""
class fun_ex_n:
    def __init__(self,n):
        self.n = n

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.n):
                result = func(*args, **kwargs)
                print(result)
        return wrapper

@fun_ex_n(8)
def split_(s):
    return s.split()


# split_('kasi')

"""positive decorator using class"""
class pos_deco:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            # print(abs(result))

        return wrapper

@pos_deco()
def add(a,b):
    return a+b
add(100,-200)

@pos_deco()
def sub(a,b):
    return a-b
# sub(500,800)

class Temp:

    def __call__(self, func):
        _cache = {}
        def wrapper(*args, **kwargs):
            if args in _cache:
                return _cache[args]
            _cache[args] = func(*args, **kwargs)
            print(_cache)
            return func(*args, **kwargs)
        return wrapper

@Temp()
def anagrams_(s1,s2):
    if sorted(s1) == sorted(s2):
        return "given inputs are angrams"
    else:
        return "not angrams"

# print(anagrams_('silent','listen'))
# print(anagrams_('kasi','jmr'))


"""count the function how many times called"""
class func_count_deco:
    def __call__(self, func):
        func.count = 0
        def wrapper(*args, **kwargs):
            func.count += 1
            result = func(*args, **kwargs)
            print(f"the {func.__name__} is called {func.count} times")
            return result
        return wrapper

@func_count_deco()
def pali_check(string_):
    res = (f"{string_}--->palindrome" if string_==string_[::-1] else f" {string_}---> not a palindrome")
    return res

# print(pali_check("malayalam"))
# print(pali_check("dad"))
# print(pali_check('kasi'))


"""write a class decoraor that raise exception if function is called n times"""
import re
class func_count_ter:
    def __init__(self, n):
        self.count = 0
        self.n = n

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.count == self.n:
                raise "maximum calls reached"
            res = func(*args, **kwargs)
            self.count += 1
            print(f"the {func.__name__} called {self.count} times")
            return res
        return wrapper

@func_count_ter(5)
def number_fetch(string_):
    return re.findall(r"\d",string_)

# print(number_fetch("kasi128rt"))
# print(number_fetch("kasi14528rt"))
# print(number_fetch("kasi128rt"))
# print(number_fetch("kasi128rt"))
# print(number_fetch("kasi128rt"))
# print(number_fetch("kasi128rt"))
#

"""single level inheritence"""
class string_opera:
    def __init__(self, s):
        self.s = s

    def split(self):
        return self.s.split()

s1 = string_opera("kasi is from guntur")

from collections import defaultdict
class ne_strings(string_opera):

    def count_words(self):
        dict_ = defaultdict(int)
        words = super().split()
        print(words)
        for word in words:
            dict_[word] += 1
        return dict_
s2 = ne_strings('python is a oops based python language')
print(s2.count_words())



"""multi level"""
class prime_gene:
    list_ = []

    @classmethod
    def numbers(cls,start,end):
        for num in range(start, end):
            cls.list_.append(num)

class prime_check(prime_gene):
    dict_ = defaultdict(list)
    @classmethod
    def prime_num(cls, num):
        for i in range(2, num):
            if num % i == 0:
                cls.dict_['not a prime'] += [num]
                break
        else:
            cls.dict_["prime"] += [num]

class ret_primes_list(prime_check):
    def primes(self):
        for num in ret_primes_list.list_:
            super().prime_num(num)
        return ret_primes_list.dict_

l = ret_primes_list()
l.numbers(10,80)
print(l.primes())












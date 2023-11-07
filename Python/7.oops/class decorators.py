"decorating each method in the class seperately by creating a decorate function and decorating inside classx"
def logging(func):
    def wraper(*args, **kwargs):
        print(f"{func.__name__} is calling")
        return func(*args, **kwargs)

    return wraper
class Arthematic:
    a = 100
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    @logging
    def add(self):
        return self.num1+self.num2
    @logging
    def mul(self):
        return self.num1 * self.num2

    def sub(self):
        return self.num1 - self.num2
c = Arthematic(10,20)
# print(c.add())

"using setattr decorating entire class"
def log(cls): # cls = Arthematic
    def logging(func): # func = value
        def wrapper(*args, **kwargs):
            print(f"{func.__name__} is calling")
            return func(*args, **kwargs)
        return wrapper
    for key, value in cls.__dict__.items():
        if callable(value):
            setattr(cls, key, logging(value)) # the output of logging(value) is wrapper address and setting that to attribute of clas
            # when a function is called wraper function is called and excecute that functiion with extra functionality
    return cls
@log  #Arthematic = log(Arthematic)
class Arthematic:
    a = 100
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1+self.num2

    def mul(self):
        return self.num1 * self.num2

    def sub(self):
        return self.num1 - self.num2
# c = Arthematic(10,20)
# print(c.add())

"""rough"""
# class a:
#     pass
# kasi = a()
# setattr(kasi, 'name', 'kasi')
# print(getattr(kasi,'name'))
# print(delattr(kasi,'name'))
# print(kasi.__dict__)
#
#
"""write a class decorator that delays each function 5 seconds"""
import time
def outer(t):
    def delay(cls):
        def spam(func):
            def wrapper(*args, **kwargs):
                time.sleep(t)
                return func(*args, **kwargs)
            return wrapper
        for key, value in cls.__dict__.items():
            if callable(value):
                setattr(cls, key, spam(value))
        return cls
    return delay
@outer(5)
class strings_:
    def __init__(self, string):
        self.string = string

    def upper(self):
        print(self.string.upper())

    def lower(self):
        print(self.string.lower())

s1 = strings_('Mohana Kasi')
s1.upper()
s1.lower()


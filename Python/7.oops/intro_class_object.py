# """"intro"""
# "int, float, complex,  ......those ale are built in classes"
# "the methods in particular classes is called as inbuilt methods "
#
# "crate our own class using class keyword"
#
#
# class Employee:
#     def __init__(self, fname, lname, pay):
#         self.first_name = fname
#         self.last_name = lname
#         self.salary = pay
# #
# "instance creation ---> instance name = classname(data or objects)"
# emp1 = Employee("kasi","s",25000) # instance creation
#
# "create a class with users and that user class has some methods"
# # class users:
# #     def __init__(self, name, bench, desig):
# #         self.name = name
# #         self.bench = bench
# #         self.desig = desig
# #
# #     def team(self):
# #
# # person1 = users('kasi','testing','QUALITY ASSUREANCE')
# # person2 = users('MOHANA','testing','QUALITY ASSURANCE')
# # person3 = users('rao','developing','junior developer')
#
#
#
#
# "__init__ is a construnctor used to create instance of a class"
# "__init__ constructor is invoked automatically when we creating instance of the class"
#
# "the data stored in instance in the form of dictionary by the constructor __init__"
#
# 'TO KNOW THE DICTIONARY OF A PARTICULAR INSTANCE ---> instance name.__dict__'
# "ex:"
# print(emp1.__dict__)
#
# "method"
# """def method name(self):
#         statement
# """
# "ex"
# class Employee:
#     def __init__(self, fname, lname, pay):
#         self.first_name = fname
#         self.last_name = lname
#         self.salary = pay
#
#     def email(self):
#         return f"{self.first_name}.{self.last_name}@gmail.com"
# emp1 = Employee("kasi","s",25000) # instance creation
# "to invoke the method syntax is ------> classname.methodnmae(particular instance name)"  "ex: employee.email(emp1)"
# "*******************(other method)****************************************************"
# "isntance name.methodname()" "ex: emp1.email()"
# "ex:"
# class Employee:
#     def __init__(self, fname, lname, pay):
#         self.first_name = fname
#         self.last_name = lname
#         self.salary = pay
#
#     def email(self):
#         return f"{self.first_name}.{self.last_name}@gmail.com"
# emp1 = Employee("kasi","s",25000) # instance creation
# # emp1.email()
#
#
# "create a class with name employee and give hike to the particular employee"
# class Employee:
#     def __init__(self, fname, lname, pay):
#         self.first_name = fname
#         self.last_name = lname
#         self.salary = pay
#
#     def hike_(self, percentage):
#         hike_amount = self.salary * percentage
#         self.salary = self.salary + hike_amount
#         return self.salary
#
#     def email(self):
#         return f"{self.first_name}.{self.last_name}@gmail.com"
# emp1 = Employee("kasi","s",25000) # instance creation
# # print(emp1.email())
# # print(emp1.hike_(0.1))
#
#
# "create a class with name Calaculator and perform some operations on numbers"
# # class Calaculator:
# #
# #     def __init__(self, value1, value2):
# #         self.a = value1
# #         self.b = value2
# #
# #     def add(self):
# #         return self.a + self.b
# #     def sub(self):
# #         return self.a - self.b
# #
# #     def mul(self):
# #         return self.a * self.b
# #
# #     def div(self):
# #         return self.a / self.b
# #
# #     def floordiv(self):
# #         return self.a // self.b
# #
# # c1 = Calaculator(10,20)
# # c2 = Calaculator(100,2500)
# # c3 = Calaculator(8,98)
# # print(c1.__dict__)
#
# # print(c1.add())
# "****or***"
# # print(Calaculator.add(c1))
# # print(c1.sub())
# # print(c2.add())
# # print(c2.sub())
# # print(c3.mul())
# # print(c1.div())
# # print(c2.div())
#
# # class bank_account:
# #     a = 'kasi'
# #     sal = 25000
# #     def __init__(self, name, balance=0):
# #         self.name = name
# #         self.balalnce = balance
# #
# # c1 = bank_account('kasi',250000) # instance creation
# # print(bank_account.sal)
# print(c1.__dict__) # instance printing
#
#
#
#
# "getting calss variables using instance"
# "instance name.__class__.varaiable name of class"
# "ex:"
#
# "*************or *******************"
# "classname.variable name iof the class"
# "ex:"
# print(bank_account.a)
#
# "to access class dictionary"
# "classname.__dict__"
# "ex:"
# # print(bank_account.__dict__)
# "or"
# "instancename (any one).__class__.__dict__"
#
# "we can access the class variable while creating instance and we can update it also"
# "so we can share the class variables among all instances and we can modify it also"
#
#
# # "shopingcart"
# # class Shopingcart:
#
# # res= [item for item in range]
# # total = sum([item for item in range(8)])
# # print(total)

# class Shopingcart:
#     products = {'motorola_g60': 3, 'laptop_hp':4, 'honor_watch':2}
#     price = {'motorola_g60':18000, 'laptop_hp':35000, "honor_watch":2500}
#
#     def __init__(self):
#         self.cart = []
#
#     def add_item(self, name_item, quantity):
#         if name_item not in Shopingcart.products:
#             raise Exception("the item is not in our list")
#         elif quantity <= Shopingcart.products[name_item]:
#             self.cart.append({"name":name_item, "quantity":quantity})
#             Shopingcart.products[name_item] -= quantity
#
#         else:
#             raise ValueError("Product out of stock")
# kasi1 = Shopingcart()
# kasi1.add_item("motorola_g60",1)
# print(kasi1.__dict__)
# # kasi1.add_item("motorola_g60",10)
# # kasi1.add_item('samsung',2)
# mohan = Shopingcart()
# mohan.add_item('honor_watch',1)
# print(mohan.__dict__)
# print(Shopingcart.products)
# # kasi1 = Shopingcart()
# # kasi1.add_item('phone',1,100)

# def loggin




# class My_name:
#     a = 10
#
# c = My_name()
# c.x = 10
# print(dir(c))
#
#
#

def log(func):
    def wraper(*args, **kwargs):
        print(f"the {func.__name__} is calling")
        result = func(*args, **kwargs)
        return result

    return wraper

def logging(some_class):
    for key, value in some_class.__dict__.items():
        if callable(value):
            setattr(some_class, key, log(value))
@logging
class Arthematic:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def add(self):
        return self.a+self.b


    def mul(self):
        return self.a*self.b


c = Arthematic()
c.__init__(10,20)

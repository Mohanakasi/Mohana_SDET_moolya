"intro"
"""python is a object oriented programing language. everything in python is an object or instance of some class\n
python class is a blueprint of an object"""

"in python oops class will have two types of variables 1)class variables 2)instance variable"
"variables present inside class will referred as class variable"
"variables present inside the instance is called as instance variables"

"when you created class variables or class methods it will imported to all instances"

"accessing class variable"
"syntax: class name.variable name"
"ex: employee.company"

"we can access the class variables using instance also"
"syntax: instance name.class variable name"
"""ex: emp1.company"""

"class example"


class Employee:
    company = "test yanthra"

    def company_(self):
        return f"company name:{self.company}"
        # print(f"accessing class variable by using instance o/p------>{self.company}")
        # print(f"accessing class variable by using instance o/p------>{employee.company}")


"instance creation"
emp1 = Employee()
emp1.company_()
# print(emp1.company_())

# print(dir(employee))
# print(dir(emp1))
"""when you create a instance it will be in the form of dictionary\n
variable name is the key and value is of value int he dictionay"""
"""checking instance dictionary"""
# print(emp1.__dict__)
# print(emp1.company_())

"""calling instance method by using the instance"""
# emp1.company_()
"""o/p ----> company name:test yanthra"""

"""calling object method by using class name"""
"""syntax: classname.instance methodnmae(instance)"""
# employee.company_(emp1)


"""adding some values into instance"""
name = 'kasi'
age = 25
sal = 25000
emp1.name = name
emp1.age = age
emp1.sal = sal
# or
emp1.name = 'kasi'
emp1.age = 25
emp1.sal = 25000
"""while assinging value to the instance you no need to define the key (varibale name) as string\n
 interepretor will implicitly takes it as string"""
# print(emp1.__dict__)
"""o/p:---->{'name': 'kasi', 'age': 25, 'sal': 25000} """

"""init comstructor"""
"""by default all the python classes will have init constructor"""
"""by suing this function we can assing values to the propoties of an object"""
"""you dont need to call this function when instance is created it will automatically callable"""

"""ex:"""
"calling decorator"


def calling_(func):
    def wraper(*args, **kwargs):
        # print(f"calling {func.__name__}")
        return func(*args, **kwargs)

    return wraper


class mobile_:
    company = 'motorola'

    @calling_
    def __init__(self, model, price):
        self.model_number = model
        self.cost = price

    @calling_
    def model_details(self):
        print(f"model number is {self.model_number}")
        print(f"price of the item is{self.cost}")


g60 = mobile_("g60", 18000)
# g60.model_details()

"""while creating values in instance init constructor and instance methods are being present in the  class dictionay"""
"""but values or attributes inside the instance will only belongs to instance only it will not be present in class dictionay"""
"""ex:"""
# print(g60.__dict__)
# print(mobile.__dict__)

"""modifying the class variables"""


def calling_(func):
    def wraper(*args, **kwargs):
        # print(f"calling {func.__name__}")
        return func(*args, **kwargs)

    return wraper


class mobile:
    company = 'motorola'

    @calling_
    def __init__(self, model, price):
        self.model_number = model
        self.cost = price

    @calling_
    def model_details(self):
        print(f"company name changed in the instance:--->{self.company}")
        print(f"company name not changed in the class:--->{mobile.company}")
        print(f"model number is {self.model_number}")
        print(f"price of the item is{self.cost}")


g40 = mobile("g40", 16000)
g40.company = 'nokia'
"""when you changes the class variable using instance it will modified in instance ditionay only"""
"""in class dictionay it will wont change it will be present as it is"""
# print(g40.__dict__)
# print(mobile.__dict__)
# g40.model_details()


"""modifying the instance values after creating it """
"example:"


class employee:
    company_ = 'qspiders'

    def __init__(self, name, sal):
        self.employee_name = name
        self.sal = sal

    def emp_details(self):
        print(f"employee name:{self.employee_name}")
        print(f"employee salary:{self.sal}")


emp1 = employee('kasi', 25000)
# print(emp1.__dict__)
# emp1.emp_details()
"""modifing"""
emp1.employee_name = 'mohana kasi'
# print(emp1.__dict__)
emp1.sal = 35000
# print(emp1.__dict__)
# emp1.emp_details()

"""deleting the instance property/ attributes"""

"we can delete the properties of an instance by using the keyword del "
"syntax: del instance name.property name/attribute name"
"example"


class mobile:
    company = 'motorola'

    def __init__(self, model, price, release_date):
        self.model_number = model
        self.cost = price
        self.release = release_date

    def model_details(self):
        print(f"model number is {self.model_number}")
        print(f"price of the item is{self.cost}")
        print(f"released on: {self.release}")


g40 = mobile("g40", 16000, "09-08-2021")
g100 = mobile("g100", 100000, "14-12-2021")
# g40.model_details()
# print()
# g100.model_details()
del g40.release
# print(g40.__dict__)

"""deleting the class attributes uisng del keyword """
# print(mobile_.__dict__)
del mobile.company
# print(mobile.__dict__)

"when you trying to access deleted attribute you get attribute error"
# print(g40.release)

"when we deleting a property of one instance will not be affected to remaining instances"
# print(g100.__dict__)

"""we can call the any class method in any class"""
"example:"
# g60.model_details()

"""we can delete any class instance or instance attribute or class attribute in any class"""
# print(employee.__dict__)
del employee.company_
# print(employee.__dict__)


"""deleting the instance or object"""


class bike:
    company_name = 'honda'

    def __init__(self, name, cc, speed, milage, cost):
        self.bike_model_name = name
        self.cc = cc
        self.speed = speed
        self.milage = milage
        self.cost = cost

    def bike_details(self):
        print(f"company:{bike.company_name}")
        print(f"bike_model: {self.bike_model_name}")
        print(f"cc:{self.cc}")
        print(f"bike top speed:{self.speed}")
        print(f"bike milage:{self.milage}")
        print(f"bike price:{self.cost}")


model1 = bike('sp_shine', 125, 120, 65, 92000)
# print(model1.__dict__)
# model1.bike_details()
model2 = bike('unicorn', 160, 150, 70, 130000)
# print(model2.__dict__)
# model2.bike_details()

del model1
"""if you acceessing the deleted instance you will get Name error"""
# print(model1.__dict__)


"""********banking class example*********************************"""


def welcome_msg(func):
    def wraper(*args, **kwargs):
        print(f"welcome to {bankaccount.bank_name} bank")
        return func(*args, **kwargs)

    return wraper


class bankaccount:
    bank_name = 'HDFC'

    def __init__(self, name, ac_number, balance=0):
        self.account_holder_name = name
        self.ac_number = ac_number
        self.balance = balance

    @welcome_msg
    def account_info(self):
        print(f"your account is created with {bankaccount.bank_name} bank successfully")
        print("check your bank account details")
        print()
        print(f"Name of the account holder: {self.account_holder_name}")
        print(f"Account Number:{self.ac_number}")
        print(f"Account Balance:{self.balance}")
        print(f"thank you for chooosing {bankaccount.bank_name} bank")

    def deposit(self, amount):
        if amount > 500:
            self.balance += amount
            print(f"the {amount} is deposited successfully")
            print(f"the current balance of your account is {self.balance}")
        else:
            raise TypeError("please try to deposit amount of more than 500")

    def withdraw(self, amount):
        if (amount <= self.balance) and amount > 3000:
            self.balance -= amount
            print(f"take the amount of {amount}")
            print(f"your current balance is {self.balance}")
        elif (amount > self.balance):
            print(f"insufficient funds")
            print(f"check your balance jaffa fellow it is {self.balance}")
        else:
            raise TypeError(f"please try to with draw the amount more than 3000")

    def transfer(self, to_number, amount):
        if (amount <= self.balance) and amount > 1000:
            self.balance -= amount
            print(f"the {amount} was transfered successfully")
            print(f"your current balance is {self.balance}")
        elif (amount > self.balance):
            raise TypeError(f"insufficient funds --->check your balance jaffa fellow it is {self.balance}")
        else:
            raise TypeError(f"please try to transfer amount of greater than 1000")


person1 = bankaccount('kasi', 50200037008003)


# print(person1.__dict__)
# person1.account_info()
# person1.deposit(300)
# person1.withdraw(100)
# person1.deposit(5000)
# person1.deposit(501)
# person1.deposit(10000)
# person1.withdraw(2000)
# person1.withdraw(8000)
# person1.withdraw(7000)
# person1.withdraw(2900)
# person1.withdraw(3001)
# person1.transfer(789858,500)
# person1.transfer(7898,8000)
# person1.transfer(7456,6500)

class shopingcart:
    products = {'motorola': 100, 'apple_watch': 30, 'apsara_pencil': 10}
    price = {'motorola': 100, 'apple_watch': 3000, 'apsara_pencil': 10}

    def __init__(self):
        self.cart = []

    def add_item(self, item_name, quantity):
        products = self.__class__.products
        price = self.__class__.price
        if item_name not in products:
            raise "item not in our store"
        elif (item_name in products) and quantity > products[item_name]:
            raise "out of stock"
        else:
            self.cart.append({"item_name": item_name, "quantity": quantity, 'price': price[item_name]})
            products[item_name] -= quantity
            # print(self.cart)

    def remove_item(self, item_name, quantity):
        for index, items in enumerate(self.cart):
            if (items['item_name'] == item_name) and (items['quantity'] == quantity):
                self.cart.remove(items)
                shopingcart.products[item_name] += quantity
            elif (items['item_name'] == item_name) and (quantity < items['quantity']):
                self.cart[index]['quantity'] -= quantity
                shopingcart.products[item_name] += quantity
            else:
                raise "given item cant found to remove in cart"
        print(f"updated cart")
        print(self.cart)

    def total_cost(self):
        print(sum([items['quantity'] * items['price'] for items in self.cart]))


kasi = shopingcart()
# kasi.add_item('apple_watch',10)
# kasi.add_item('nokia',80)
# kasi.add_item('motorola',5)
# print(kasi.cart)
# print(shopingcart.products)
# kasi.remove_item('apple_watch',5)
# print(shopingcart.products)
# kasi.total_cost()
# kasi.add_item('apsara_pencil',5)
# kasi.total_cost()
# print(shopingcart.products)
# kasi.remove_item('apsara_pencil',2)
# kasi.total_cost()


"""inheritence"""

class Bankaccount:
    # interest rate = 0.04
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.statement = [f"***********stetement of {self.name}***********************"]

    def deposit(self, amount):
        if amount <= 0:
            raise "deposit amount greater than 0"
        print(f"deposit of {amount} was successful")
        self.balance += amount
        print(f"current balance is {self.balance}")
        self.statement.append(f"****deposit of {amount} on date, ---> current balance:{self.balance}*****")
    def withdraw(self, amount):
        if amount > self.balance:
            raise f"insufficient funds"
        elif amount == 0 or amount < 0:
            raise f"enter the amount greater then {amount}"
        print(f"with draw of {amount} was successful")
        self.balance -= amount
        print(f"current balance is {self.balance}")
        self.statement.append(f"****withdrawl of {amount} on date, ---> current balance:{self.balance}*****")



person1 = Bankaccount('kasi')
# print(person1.__dict__)
# person1.deposit(100)
# print(person1.__dict__)
# person1.withdraw(100)
# person1.deposit(10000)
# person1.withdraw(10)
# person1.withdraw(1000)

""
class savingsaccount(Bankaccount):
    def deposit(self, amount):
        if amount <= 1000:
            raise "deposit amount greater then or equal to 1000"
        super().deposit(amount)

    def withdraw(self, amount):
        if amount <= 3000:
            raise "plese enter the amount greater then 3000"

        super().withdraw(amount)
        if self.balance < 1000:
            self.balance -= 200

p1 = savingsaccount('kasi')
# p1.deposit(10000)
# p1.withdraw(10000)
# print(p1.get_statement())
# print(p1.balance)

# class current(Bankaccount):
#     def deposit(self, amount):
#         if amount < 10000:
#             raise "current account minimum deposit is 10000"
#         super().deposit(amount)
#
#     def withdraw(self, amount):
#         if amount < 5000:
#             raise "current account withdrawl balance is 5000"
#         super().withdraw(amount)
#
#
# c1 = current('mohana kasi')
# c1.deposit(15000)
# c1.withdraw(5000)
# c1.withdraw(10000)
# c1.withdraw(10)

# class Salaryaccount(Bankaccount):

#
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f'Calling decorator {func.__name__}')
#         return func(*args, **kwargs)
#     return wrapper
# def logging(cls):
#     for key, value in cls.__dict__.items():
#         if callable(value):
#              setattr(cls, key, log(value))
#     return cls

a = 100
def func():
    pass
func()
print(callable(a))
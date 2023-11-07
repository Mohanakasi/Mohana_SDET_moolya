"""encapsulation"""
class temp:
    __a = 10
    __b = 20

    def get_a(self):
        print(self.__a)
    def set_a(self,value):   # it will modifies in object only
        self.__a = value

# s = temp()
# s.get_a()
# s.set_a(50)
# s.get_a()

"""property decorator  in encapsulation"""
"""using old"""
class sample:
    __a = 10
    __b = 20

    def get_a(self):
        return self.__a
    def set_a(self,value):   # it will modifies in object only
        self.__a = value

    pro = property(get_a,set_a)

# s = sample()
# print(s.pro)
# s.pro = 50
# print(s.pro)



"""property (using property decorator)"""
"""by using the property decorator we can give access the user to access the protected variables anf 
if you want to restrict to modify the protected variables and deletig it"""
class Temp:
    __a = 10
    __b = 20

    @property
    def var_a(self):
        return self.__a
    @var_a.setter
    def var_a(self,value):
        raise ValueError

    @var_a.deleter
    def var_a(self):
        del self.__a

# s1 = Temp()


"""polymorphisam"""
"""single function different ways of performance"""

"""ex: len()"""
"""len(str) ---> no of charcters in a string"""
"""len(list,tuple) ---> no of items in a list, tuple"""
"""len(set, dict) ---> no of keys in a set, dict"""

"""operators"""
"+ operator"
"for numeric data types it will adds the values"
"""in case of collection data types it concatinates it"""

"* operator"
"""for numeric data types it will multiply the values and gives the value aas output"""
"""in case of collection data types it print that dat type for multiple tiems"""
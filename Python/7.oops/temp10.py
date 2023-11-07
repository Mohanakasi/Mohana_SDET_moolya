# class Strings:
#     def __init__(self, string_name):
#         self.string_name = string_name
#     def reverse_(self):
#         a = self.string_name[::-1]
#         return a
#     def upper_(self):
#         b = self.string_name.upper()
#         return b
# c1 = Strings("Kashi")
# print(c1.reverse_())
# print(c1.upper_())

# class Even_odd:
#     def __init__(self, num1):
#         self.num1 = num1
#     def eo(self):
#         if self.num1 % 2 == 0:
#             print(f"{self.num1} is even")
#         else:
#             print(f"{self.num1} is odd")
# c1 = Even_odd(96)
# c1.eo()

#
# class Com_branch1:
#     company_name = 'Capgemini'
#     def __init__(self, name, loc, desi):
#         self.name = name
#         self.loc = loc
#         self.desi = desi
#
#     def get_data(self):
#         print(f"employee name is:{self.name}")
#         print(f"employee loc is :{self.loc}")
#         print(f"employee designation: {self.desi}")
#
# emp = Com_branch1('chandana', 'mumbai', 'ceo')
# # print(emp.__dict__)
# # emp.get_data()
# print(Com_branch1.__dict__)
# class Delta(Com_branch1):
#     def __init__(self, name, loc, desi, sal):
#         self.sal = sal
#         super().__init__(name, loc, desi)
#
#
# e1 = Delta('kasi', 'guntur', 'automation engineer',1000)
# e1.get_data()
# print()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#



a = 10
class spam:
    def add(self):
        # a += 1
        return a

s = spam()
print(s.add())
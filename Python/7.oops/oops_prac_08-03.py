class employee:
    company = 'test yanthra'
    def __init__(self, name, age, sal):
        self.employee_name = name
        self.employee_age = age
        self.salary = sal

    def emp_details(self, location):
        print(self.company)
        print(f"employee name is:{self.employee_name}")
        print(f"employee age:{self.employee_age}")
        print(f"employee salary is {self.salary}")
        print(f"employee location is: {location}")

e1 = employee('kasi',25,700000)
# e1.emp_details('bangalore')
e2 = employee('rao',28,560000)
# e2.emp_details('chennai')
# print(e1.__dict__)
# e1.company = 'tcs'
# print(employee.company)
class split_:
    def __init__(self, string_):
        self.string_name = string_

    def oper_(self):
        return self.string_name.split()

s1 = split_('kasi is in bamgalore')
# print(s1.oper_())

from collections import defaultdict
# d = defaultdict(int)
# d['kasi'] = 3000
# class count_words:
#     def __init__(self,s):
#         self.s=s
#
#     def words_count(self):
#         d['kasi'] = 100
#         d['kasi'] = 10000
#         print(d)
#         res = self.s.split()
#         # for word in res:
#         #     d[word] +=1
#         # print(d)
# a1 = count_words('kasi is')
# a1.words_count()



# class list_:
#     def __init__(self, l):
#         self.l = l
#
#     def oper_(self):
#         for item in self.l:
#             if isinstance(item, str):
#                 print(item[::-1])
#
#
# l1 = list_(['python','kasi',8.8,{7,8,9,},{'a':10}])
# l1.oper_()

from selenium.webdriver.common.by import By

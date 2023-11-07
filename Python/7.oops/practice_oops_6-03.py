"""program to print only numbers in a list"""
class nums_list:
    def __init__(self, list_):
        self.list_ = list_

    def nums_(self):
        for item in self.list_:
            if isinstance(item, int):
                print(item)

obj = nums_list([1,2,'kasi',2020,'jmr'])
# obj.nums_()

"""write a program to create a dictionary with word it's count pair in a string"""
from collections import defaultdict
class count_words:
    def __init__(self, string_):
        self.string_ = string_
        self.dict_ = defaultdict(int)

    def dict_words(self):
        for word in self.string_.split():
            self.dict_[word] += 1
        return self.dict_

s = count_words('python boomeranging the world python')
# print(s.dict_words())

"""printing if string in a list of  even lenth as is it is , if it is odd length reverse the string"""
# creating a new list
# class list_op:
#     def __init__(self, list_):
#         self.list_ = list_
#
#     def string_eve_rev(self):
#         res = [item if len(item) % 2 == 0 else item[::-1] for item in self.list_]
#         return res
#
# l1 = list_op(['kasi','python','bangalore'])
# print(l1.string_eve_rev())

"""modifying the old list"""
class list_op:
    def __init__(self, list_):
        self.list_ = list_

    def string_eve_rev(self):
        for index,item in enumerate(self.list_):
            if len(item) % 2 == 0:
                self.list_[index] = item
            else:
                self.list_[index] = item[::-1]
        return self.list_

l1 = list_op(['mohana kasi','jmr','chandana'])

l1 = list_op(['kasi','python','bangalore'])
# print(l1.string_eve_rev())

"""create a class to count the no of characters present in a string without using len function"""
class cha_co:
    count = 0
    @classmethod
    def __call__(self, string_):
        print(cha_co.count)
        for char in string_:
            self.count += 1
        return cha_co.count

s = cha_co()
# print(s('kasinadh'))

"""write a program to print all the palindromes in a list"""
class list_op:
    def __init__(self, list_):
        self.list_ = list_

    def __call__(self):
        for item in self.list_:
            if item == item[::-1]:
                print(item)
# s = list_op(['malayalam','dad'])
# s()


"""write a program to create a dictionary with word and it's length pair only if thr word is of even length"""
class temp:
    dict_ = {}
    @classmethod
    def ev_len(cls,string_):
        for word in string_.split():
            if len(word) % 2 == 0:
                cls.dict_[word] = len(word)
        print(cls.dict_)


s = temp()
# s.ev_len('mohana kasi is from guntur')

"""create a list of tuples which is having index and it's corresponing item"""
class Comprehe_:

    def __call__(self, list_):
        res = [(index,item) for index, item in enumerate(list_)]
        return res

s = Comprehe_()
# print(s('python is a oops based language'.split()))

"""write a program to create a list if the item in the list of string else reverse it"""
class comprehe_2:
    def __call__(self, list_):
        res = [item if isinstance(item, str) else str(item)[::-1] for item in list_]
        return res


# print(comprehe_2()(['mohana kas',2020,1008456]))
l = comprehe_2()
# print(l(['mohana kas',2020,1008456]))

"""create a dictionary with it's word and count pair"""
class dict_compre:
    @staticmethod
    def word_count(string_):
        list_ = string_.split()
        dict_ = {word:list_.count(word) for word in list_}
        return dict_
    @staticmethod
    def word_even_len(string_):
        dict_ = {word:len(word) for word in string_.split() if len(word) % 2 == 0}
        return dict_
    def item_ind_pair(self,list_):
        dict_ = {index:item[::-1] if isinstance(item, str) else item for index, item in enumerate(list_)}
        return dict_
# d = dict_compre()
# # print(d.word_count('rain is falling from morning but sill rain is not quit'))
# d1 = dict_compre()
# # print(d1.word_even_len('this phone is very heavy'))
# d2 = dict_compre()
# print(d2.item_ind_pair(['kasi',1008,7897,'jmr']))

# def temp:
#     string_ = 'new account'
#
#     @classmethod
#     def samp(cls):



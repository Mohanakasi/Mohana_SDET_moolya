# # # stirng_ = 'this is 124Mohana'
# # # stirng2_ = '1234'
# # # print(stirng_.isalnum())
# # # # print(stirng2_.isalnum())
# #
# # print('12is'.isidentifier())
# # print('_12fr'.isidentifier())
#
#
# # print(type(45))
# # print(type(''))
# # print(dir(int))
#
# string_ = 'Mohana'
# # print(string_[3::2])
# # print(ord('0'), ord('9'))
# # print(90-122)
# # for num in range(65,91):
# #     print(chr(num))
#
# # string_ = 'this is 2nd 8 7 634 %%$# -mohsna'
# # for char in string_:
# #     if 48 <= ord(char) <= 57:
# #         print(char, 'nmber')
#
# count_ = 0
# count2 = 0
# string_ = 'This is mohana'
# for char in string_:
#     if char == 'i':
#         count_ += 1
#     if char == 's':
#         count2+= 1
#
# print(count_, count2)
# print(string_.count('s'))
#
#
# string_ = 'this is kasi'
# for index in range(len(string_)):
#     print(index, string_[index])
#
# index = -1
# string_ = 'this is kasi'
# for char in string_:
#     index += 1
#     print(char, index)
#
# index = -1
# string_ = 'this is kasi'
# for char in string_:
#     index += 1
#     if char == 's':
#         print(char, index)
# #
# #
# # list_ = [(1,2),(3,4)]
# # item1, item2 = list_[0] #(1,2)
# # print(item1, item2)
# # # for item1, item2 in list_:
# # #     print(item1)
# # #     print(item2)
# #
# #
# # dict_ = {}
# # lsit_ = ['flight', 'fan', 'fright', 'fan', 'bike']
# # for string_ in lsit_:
# #     for char in string_:
# #         if char in dict_:
# #             dict_[char] += 1
# #         else:
# #             dict_[char] = 1
# #     print(dict_)
# # from collections import defaultdict
# # dict_ = defaultdict(int)
# #
# # for string_ in lsit_:
# #     for char in string_:
# #         dict_[char] += 1
# #     print(dict_)
#
# strin_ = 'kasi is from gungtr'
# for char in string_:
#     print(char)
# for index, char in enumerate(strin_):
#     print(char, index)
#
# print(strin_.split())
#
# list_ = ['this', 'is', 'mohana']
# print('$'.join(list_))
#
#
# string_ = '***+:: kasi * +++ Madhu love forever*&&&&***'
# print(string_.strip('*'))
# print(string_.lstrip('*'))
# print(string_.rstrip('*'))
#
# string_ = 'c1'
# print(string_.isalnum())
# strin_ = 'CHaR'
# print(strin_.isupper())
#
# string_ = 'This is gunt8ir'
# for char in string_:
#     if char.islower() and isinstance(char, str):
#         print(chr(ord(char)-32))

for num in range(0, 10):
    print(ord(str(num)))
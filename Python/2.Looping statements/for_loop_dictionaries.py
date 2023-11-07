
"""traversing through dictionary directly"""
# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# for key in d:
#     print(key, end=" ")
# print()

"""printing keys using keys inbuilt method  """
# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# for key in d.keys():
#     print(key, end=" ")
# print()

"""printing keys using items inbuilt method"""
# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# for key, value in d.items():
#     print(key, end=" ")


"""print values in a dictionary"""
# dict_ = {'a':10,"b":20, "c":30}
# for value in dict_.values():
#     print(value,end = ' ')

"""print values in a dictionary using get method"""
# for key in dict_:
#     print(dict_.get(key))

"""print values in a dictionary  using enumerate class"""
# print("indice, '..,key,'...',value")
# for indice,(key,value) in enumerate(dict_.items()):
#     print(indice, '....',key,'...',value)

"""printing characters and its count of a string into dictionary uisng inbuilt method count"""
# s = 'hello world'
# d ={}
# for char in s:
#     if char not in d:
#         d[char] = s.count(char)
# print(d)


"""printing characters and its count of a string into dictionary without using inbuilt method (if - else)"""
# s = 'hello world'
# d ={}
# for char in s:
#     if char not in d:
#         d[char] = 1
#     else:
#         d[char] += 1
#
# print(d)

"""printing characters and its count of a string into dictionary without using inbuilt method (two for loops)"""""
# s = 'hello world'
# d ={}
# for i in s:
#     count = 0
#     for j in s:
#         if i == j:
#             count += 1
#     d[i] = count
# print(d)


"""printing characters and its count of a string into dictionary using inbuilt class defaultdict"""
# from collections import defaultdict
# s = 'hello world'
# dd = defaultdict(int)
# for i in s:
#     dd[i] = dd[i]+1
# print(dd)

"""counting no words in a string and printing with word and count into  a dictionary 
using without inbuilt (if-else)"""
# s = 'python has python inbuilt modules'
# string_ = s.split()
# d = {}
# for word in string_:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] = d[word]+1
# print(d)
#
"""counting no words in a string and printing with word and count into  a dictionary using inbuilt method count"""
# s = 'python has python inbuilt modules'
# string_ = s.split()
# d = {}
# for word in string_:
#     d[word] = s.count(word)
# print(d)


"""counting no words in a string and printing with word and count into  a dictionary using two for loops"""
# s = 'python has python inbuilt modules'
# string_ = s.split()
# d = {}
# for i in string_:
#     count = 0
#     for j in string_:
#         if i == j:
#             count += 1
#     d[i] = count
# print(d)

"""counting no words in a string and printing with word and count into  a dictionary using inbuilt class"""
# from collections import defaultdict
# s = 'python has python inbuilt modules'
# string_ = s.split()
# dd = defaultdict(int)
# for word in string_:
#     dd[word] = dd[word] + 1
# print(dd)



"""counting  words in a string and printing with word and length into  a dictionary"""
# s = 'python has python inbuilt modules'
# string_ = s.split()
# d = {}
# for word in string_:
#     d[word] = len(word)
# print(d)

"""counting  words in a string and printing with word and length into  a dictionary"""
# s = 'python has python inbuilt modules'
# string_ = s.split()
# d = {}
# for word in string_:
#     d[word] = len(word)
# print(d)



"""printing words and its lenth of string (if word is even) into  dictionary without using inbuilt methods"""
# s = 'python has inbuilt modules anid a powerful oops '
# list_ = s.split()
# d = {}
# for word in list_:
#     if len(word) % 2 == 0:
#         d[word] = len(word)
# print(d)


"""printing words and its lenth of string (if word is even) into  dictionary (if word starting with vowel)"""
# s = 'Oython has inbuilt Eodules anid a powerful oops '
# list_ = s.split()
# d = {}
# for word in list_:
#     if word[0] in 'aeiouAEIOU':
#         d[word] = len(word)
# print(d)


"""printing words and its count of string into dictionary if the word is not repeated  in string"""
# s = 'python has python inbuilt modules anid it has powerful oops '
# list_ = s.split()
# d = {}
# for word in list_:
#     if list_.count(word) == 1:
#         d[word] = list_.count(word)
# print(d)



"""printing first letter of a word in a string as key and that word as list of word (using defaultdict class)"""
# from collections import defaultdict
# sent = 'hello world welcome to python programmming hi there'
# list_ = sent.split()
# dd = defaultdict(list)
# for word in list_:
#     dd[word[0]] += [word]
# print(dd)

"""printing first letter of a word in a string as key and that word as list of word"""
# sent = 'hello world welcome to python programmming hi there'
# list_ = sent.split()
# d = {}
# for word in list_:
#     if word[0] not in d:
#         d[word[0]] = [word]
#     else:
#         d[word[0]] += [word]
# print(d)


"""printing dictionary with items and it's index values of  a list"""
# list_ = ['apple','google','gmail','apple']
# d={}
# for index,item in enumerate(list_):
#     if item not in d:
#         d[item] = [index]
#     else:
#         d[item].append(index)
# print(d)

"""printing dictionary with items and it's index values of  a list"""
# from collections import defaultdict
# list_ = ['apple','google','gmail','apple']
# dd = defaultdict(list)
# for index,item in enumerate(list_):
#     dd[item] += [index]
# print(dd)

"""swaping keys and values using items method"""
# d = {'a': 1, 'b': 2, 'c':3, 'd': 4}
# d2 = {}
# for key,value in d.items():
#     d2.update({value:key})
# print(d2)

"""swaping keys and values using items method"""
# d = {'a': 1, 'b': 2, 'c':3, 'd': 4}
# d2 = {}
# for key,value in d.items():
#     d2[value] = key
# print(d2)

a = 20
# for _ in range(1,2):
#     a += 10
# print(a)
for _ in range(1,2):
    for j in range(1,2,):
        a += 50
print(a)

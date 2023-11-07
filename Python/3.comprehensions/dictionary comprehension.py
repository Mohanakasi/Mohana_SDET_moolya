""" WAP to create a dictionary with item and its index pair"""

"""normal method"""
# string = "hello"
# d = {}
# for index, item in enumerate(string):
#     d[item] = index
# print(d)

# comprehension
# string = "hello"
# dict_ = {item: index for index, item in enumerate(string)}
# print(dict_)

""" WAP to create a dictionary with word and its length pair"""
"""normal method"""
# string_ = 'kasi nadh'
# words = string_.split()
# d = {}
# for word in words:
#     d[word] = len(word)
# print(d)

"""using dictionary comprehension"""
# string_ = 'kasi nadh'
# dict_ = {word: len(word) for word in string_.split()}
# print(dict_ )

#******************************************************************
"""word and it's count pair"""
"""(normal method)"""
# s = 'kasi nadh is a king of kasi palace'
# d = {}
# words = s.split()
# for word in words:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] += 1
# print(d)

"""(using default dictionary)"""
# from collections import defaultdict
# s = 'kasi nadh is a king of kasi palace'
# dd = defaultdict(int)
# words = s.split()
# for word in words:
#     dd[word] += 1
# print(dd)

"""using dict comprehension"""
# s = 'kasi nadh is a king of kasi palace'
# words = s.split()
# dict_ = {word:s.count(word) for word in words}
# print(dict_)
"""*************************************************************************"""
"""printing dictionaryu with word and its count pair only if word is of even length"""
"""(normal method)"""
# s = 'kasi nadh is a king of kasi palace'
# d = {}
# words = s.split()
# for word in words:
#     if len(word) % 2 == 0:
#         d[word] = s.count(word)
# print(d)

"""(using default dict)"""
# from collections import defaultdict
# s = 'kasi nadh is a king of kasi palace'
# words = s.split()
# dd = defaultdict(int)
# for word in words:
#     if len(word) % 2 == 0:
#         dd[word] += 1
# print(dd)

"""(using list comprehension)"""
# s = 'kasi nadh is a king of kasi palace'
# words = s.split()
# dict_ = {word:s.count(word) for word in words if len(word) % 2 ==0}
# print(dict_)


""" take key as index and words as values if the word in a string is of odd lenth reverse it else keep as iti is"""
"""(using normal method)"""
# s = 'kasi nadh is a king of kasi palace'
# words = s.split()
# d = {}
# for index,word in enumerate(words):
#     if len(word) % 2 != 0:
#         d[index] = word[::-1]
#     else:
#         d[index] = word
# print(d)

"""(using dictionary comprehension)"""
# s = 'kasi nadh is a king of kasi palace'
# words = s.split()
# dict_ = {index:word[::-1] if len(word) %2 != 0 else word for index,word in enumerate(words)}
# print(dict_)



"""(creating a dictionary with word and it's length psir if word is starting with vowel)"""
# s = 'kasi nadh is a king of kasi palace'
# dict_ = {word:len(word) for word in s.split() if word[0].lower() in 'aeiou'}
# print(dict_)


"""to create a dictionary with index and item pair if the item is o string data type reverse it 
else keep it as it is"""
# list_ = ['kasi',108,True,'nadh']
# dict_ = {index:item[::-1] if isinstance(item,str) else item for index,item in enumerate(list_)}
# print(dict_)

"""to create a dictionary with item and index pair if the item is o string data type keep it as it is 
else reverse it"""
# list_ = ['mohana','kasi','jmr',1008,50+50J,True]
# dict_ = {index:item if isinstance(item,str) else str(item) [::-1] for index,item in enumerate(list_)}
# print(dict_)

"""swaping keys and values"""
# d  = {'a':1,"b":2,'c':30}
# dict_ = {d[key]:key for key in d}
# print(dict_)

"""using items method"""
# dict_ = {item:key for key,item in d.items()}
# print(dict_)


""" char and ascii value pair """
# string = "python"
# d = {char: ord(char) for char in string}
# print(d)


# list_ = ['kasi','kasi','kasi','123']
# d = {}
# for key in list_:
#     if key not in d:
#         d[key] = 1
#     else:
#         d[key] += 1
# print(d)
#
# dd ={key: 1 if key not in d else +1 for key in list_}
# print(dd)

d  = {'a': 1, 'b':2 }
dd = {d[key]+: key for key in d}
print(dd)
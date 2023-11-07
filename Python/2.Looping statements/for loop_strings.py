
""'print 1 to 10using for loop""'
# for num in range(1,11):
#     print(num)

"""print 10 to 1 using for loop"""
# for num in range(10,0,-1):
#     print(num)

"""print -1 to -10 using for"""
# for num in range(-1,-11,-1):
#     print(num)

"""print even numbers using for loop"""
# for num in range(1,11):
#     if num % 2 == 0:
#         print(num)


# for num in range(2,11,2):
#     print(num)

"""trravels throuh string using for loop"""
# string_ = 'kasi is a king'
# for val in range(len(string_)):
#     print(string_[val],end='')


"""trravels throuh string using for loop (appending string istead of range())"""
# string_ = 'kasi is a king'
# for val in string_:
#     print(val,end='')

"""trravels throuh list using for loop"""
# # list_ = [1,2,3,'kasi']
# # for val in range(len(list_)):
# #     print(list_[val],end=' ')

"""trravels throuh list using for loop (appending list  instead of range )"""
# list_ = [1,2,3,'kasi']
# for val in list_:
#     print(val,end=' ')

"""traversing through set"""
# set_ = {1,2,1008,'kasi'}
# for key in set_:
#     print(key)

"""traversing throung set using type conversion"""
# set_ = {'ksi','rao',1008}
# list_ = list(set_)
# for val in range(len(list_)):
#     print(list_[val])

""" traversing through dictionaries """
# d = {"one": 1, "two": 2, "three": 3}
#
# for key in d:
#     print(key, d[key], sep="-->")
"""unpacking"""
# a=[1,2,3,4]
# n1,*rest,n2=a
# print(*resst,n1,n2)



""" to print index and character in a string """
# s = "hello"

# for item in range(len(s)):
#     print(item, s[item])

# for index, item in enumerate(s):
#     print(index, "-->", item)

""" traversing a string in reversed order """
# string = "hai"

# for item in range(len(string)-1, -1, -1):
#     print(string[item], end=" ")
#
# print()
#
# for char in string[::-1]:
#     print(char, end=" ")
#
# print()
# for item in reversed(string):
#     print(item, end=" ")


""" count the number of characters in a string """
# string = "hello world"

# count = 0
# for _ in string:
#     count += 1

# print(count)


"""print even characters in a string"""
# s = 'hello'
# for item in s:
#     if s.find(item)%2 == 0:
#         print(item,end=' ')


"""to print the digits in a string using inbuilt method"""
# s= 'kasi 123'
# for item in s:
#     if item.isdigit():
#         print(item)

#
"""print numbers in a string using without inbuilt"""
# s = 'hello 1223'
# for item in s:
#     if '0' <= item <= '9' :
#         print(item)

"""to count no of special characters in a string"""
# string_ = 'kasi123@$$$.%+    '
# count = len(string_)
# for item in string_:
#     if (item.isalpha()) or (item.isdigit()) :
#             count -= 1
# print(f"count of special characters is {count}")


"""to count capital and small letters in a string"""
# string_ = 'KASI is from GUNTUR'
# count1_ = 0
# count2_ = 0
# for item in string_:
#     if item.islower():
#         count1_ += 1
#     elif item.isupper():
#         count2_ += 1
# print(f"the string has {count1_} small letters")
# print(f"the string has {count2_} capital letters")


"""program to count no of special characters in a string"""
# string_ = r'kasi123@$$$///\\%+'
# count = len(string_)
# for item in string_:
#     if (item.isalpha()) or (item.isdigit()) :
#             count -= 1
# print(count)
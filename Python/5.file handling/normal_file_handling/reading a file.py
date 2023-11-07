import os
from collections import *
"""reading a file"""
"using read"
# it reads the data from starting to end of the file
path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\sindhu12.txt"
# with open(path) as file:
#     print(file.read()) # in read we may pass index no (index no is optional)
#     data = file.read()
#     print(data)
#     print(file.tell())
#     print(file.seek(50))
#     print(file.read())

"""uisng read line"""
# readline() reads one line at atime. in readline also we can pass indexing
# if given index no is below the line it will print upto that index no
# with open(path) as file:
#     file.seek(6)
#     print(file.readline())

""""uisng read lines"""
# with open(path) as file:
#     print(file.readlines())

"wap to read all the lines in a file without loading the file into memory"
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             print(line)

"wap to count the no of lines present in the file"
# with open(path) as file:
#     count = 0
#     for line in file:
#         if line.strip():
#             count += 1
#     print(count)

"""wap to print line and line no from the file"""
"""normal method"""
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         print(line, count)

"using enumerate"
# with open(path) as file:
#     for lineno,line in enumerate(file):
#         print(line,lineno)


"""wap to count the no of words in a given file"""
# with open(path) as file:
#     count = 0
#     for line in file:
#         list_ = line.split()
#         count += len(list_)
#     print(count)

"""wap to print the file from the last oif the file"""
# with open(path) as file:
#     for rline in reversed(list(file)): # we cant apply reversed class on file object we have to type cast the file object
#         print(rline)

"""wap to count the no of words that are starting with vowels"""
# with open(path) as file:
#     count  = 0
#     for line in file:
#         words = line.split()
#         for word in words:
#             if word[0].lower() in 'aeiou':
#                 count += 1
#     print(count)

"""wapto count the no of spaces in the file"""
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += line.count(' ')
# print(count)

"""wap to count word and it's count pair in the given list"""
# with open(path) as file:
#     d = defaultdict(int)
#     for line in file:
#         if line.strip():
#             words = line.split()
#             for word in words:
#                 d[word] += 1
#     print(d)


#
# string_ = 'kasi is a kasi nadh python kasi nadh'
# words = string_.split()
# print(Counter(words))

"""wap to group ip addresses and it's count"""
path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\text files\access-log.txt"
# with open(path) as file:
#     l = []
#     for line in file:
#         if line.strip():
#             words = line.split()
#             l.append(words[0])
#     ip_ = Counter(l) # Counter is a class available in collections which will count of each word in a list and returns
#     print(ip_)      # in the form of dictionary
#     print(ip_.most_common(1)) # using most_commo() we can pass n arguments which print n most common word count pairs

"""wap to print nth line in a file"""
"""using enumerate"""
# with open(path) as file:
#     n = 10
#     for lineno,line in enumerate(file):
#         if line.strip():
#             if lineno == n:
#                 print(line)
#                 break
"""using islice"""




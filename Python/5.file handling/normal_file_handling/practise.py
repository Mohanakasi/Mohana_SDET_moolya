import os
from collections import defaultdict
from itertools import islice
from collections import Counter
from collections import deque
import csv

path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\text files\sindhu12.txt"
"write a program to count the no of line in a file"
# with open(path) as file:
#     line_no = 0
#     for line in file:
#         line_no += 1
#     print(f"the no of line in the file is {line_no}")

"write a program to print the line and line no from the file"
"normal metod"
# with open(path) as file:
#     line_no = 0
#     for line in file:
#         print(line_no, line, sep="---->")
#         line_no += 1

"using enumearte"
# with open(path) as file:
#     for line_no, line in enumerate(file):
#         print(line_no, line, sep="---->")

"to count the no of words in a file"
# with open(path) as file:
#     words_count = 0
#     for line in file:
#         words_count += len(line.split())
#     print(words_count)

"write a program to print thge file from the last"
# with open(path) as file:
#     for line in reversed(list(file)):
#         print(line)

"write a program to count the no of spaces in the file"
"normal method"
# with open(path) as file:
#     space_count = 0
#     for line in file:
#         for char in line:
#             if char == ' ':
#                 space_count += 1
#     print(space_count)

"using count inbuilt method"
# with open(path) as file:
#     space_count = 0
#     for line in file:
#         space_count += line.count(' ')
#     print(space_count)

"convert each line in the file to uppercase"
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             print(line.upper())

"to convert the each line in the file into lower"
# with open(path) as file:
#     for line in file:
#         print(line.lower())

"write a program to count the no of words that are startring with vowels"
# with open(path) as file:
#     words_vow_count = 0
#     for line in file:
#         words_list = line.split()
#         for word in words_list:
#             if word[0].lower() in 'aeiou':
#                 words_vow_count += 1
#     print(words_vow_count)

"write a program to create a dictionary of word and it's count pair"
# with open(path) as file:
#     dict_file = defaultdict(int)
#     for line in file:
#         words_list = line.split()
#         for word in words_list:
#             dict_file[word] += 1
#     print(dict_file)

"wap to extract all ip address from access log text file"
# path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\text files\access-log.txt"
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             words_list = line.split()
#             print(words_list[0])

"ipaddress and it's count pair" # using counter class
# with open(path) as file:
#     l = []
#     for line in file:
#         if line.strip():
#             words_list = line.split()
#             l.append(words_list[0])
#
#     ip_ = Counter(l) # Counter class will convert a list of words into dictionary of words and it's count pair(decending order)
#     print(ip_)

"to print nth line in the file"

n = 5
"using normal method"
# with open(path) as file:
#     count = 0
#     for line in file:
#         if count == n:
#             print(line)
#             break
#         else:
#             count += 1
"using enumerate method"
# with open(path) as file:
#     for line_no, line in enumerate(file):
#         if line_no == n:
#             print(line)
#             break

"using islice"
with open(path) as file:
    res = islice(file, n-1, n)
    # print(*list(res))

"to print n lines in the file"
n = 3
# with open(path) as file:
#     res=islice(file, n)
#     print(*list(res))

"""deque"""
# "to print last  n lines in a file"
# n = 2
# with open(path) as file:
#     res = deque(file, n)
#     print(*list(res))

"to find nth line or n lines we have to use islice"
"to find last n lines  we have to use deque"


"******************************************************************************************"
"****************************csvfiles******************************************************"
"******************************************************************************************"

"csv.reader holds the data in the form of list"
path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\csv_files\employees.csv"
# with open(path) as csv_file:
#     row_obj = csv.reader(csv_file) # we have to convert csv file to row object using csv.reader()
#     for row in row_obj:
#         print(*row)

"skipping headder"
# with open(path) as csv_file:
#     row_obj = csv.reader(csv_file)
#     next(row_obj)
#     for row in row_obj:
#         print(*row)

"wap to print only employee names in the employee file"
# with open(path) as csv_file:
#     row_obj = csv.reader(csv_file)
#     next(row_obj)
#     for row in row_obj:
#         if row: # if your file has any empty lines it wont throw any error if use this if condition
#             print(row[0])

"wap to print employee names only the names with salary greater than 70000"
# with open(path) as csv_file:
#     row_obj = csv.reader(csv_file)
#     next(row_obj)
#     for row in row_obj:
#         if row:
#             # print(type(row[1])) #in csv file each row is a type list and each element in each row is a ype string
#             if int(row[-1]) > 70000:
#                 print(row[0])

"write a program to group male and female employees"
# with open(path) as csv_file:
#     dict_ = defaultdict(list)
#     row_obj = csv.reader(csv_file)
#     next(row_obj)
#     for row in row_obj:
#         if row:
#             dict_[row[1]] += [row[0]]
#
#     print(dict_)

"write a program to group the employees based on their teams"
# with open(path) as csv_file:
#     dict_ = defaultdict(list)
#     row_obj = csv.reader(csv_file)
#     next(row_obj)
#     for row in row_obj:
#         if row:
#             dict_[row[2]] += [row[0]]
#
#     print(dict_)

"wap to sort the shares in the test.csv file based on prices"
path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\csv_files\test.csv"
"using csv.reader()"
# with open(path) as csv_file:
#     read_obj = csv.reader(csv_file)
#     next(read_obj)
#     l = list(read_obj)
#     res = sorted(l, key =lambda item:float(item[-1]))
#     print(res)

"using csv.DictReader"
with open(path) as csv_file:
    read_obj = csv.DictReader(csv_file)
    # next(read_obj)
    l = list(read_obj)
    res = sorted(l, key = d:float(d["price"])
    print(list(res))






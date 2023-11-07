"getting ccurrent working directory"
# import os
# print(os.getcwd())
"making a new directory"
# os.mkdir(r"C:\kasi_king")
# os.mkdir(r"C:\kasipython")

"changing currenet directory to some other directory"
# os.chdir(r"C:\Users\Hp\PycharmProjects\python_training\5.file handling\normal_file_handling\new")
# print(os.getcwd())

# os.rmdir(r"C:\kasi_king")
# os.rmdir(r"C:\kasipython")

"list directories"
# print(os.listdir(r"D:"))
# print(os.listdir(r"E:"))

# os.chdir(r"D:\PENDRIVE BACKUP\SANDISK 64 GB\CREATIVE STUDIO\9-8-2020\JULY  DATA   (15581)\GIVEN TO VRDL STAFF\9-8-2020\MY FINAL")
# "opening a file from python file"
# os.popen(r"temp.csv",'r')
# file = open("madhuri.txt",'w')
# os.chdir(r"C:\Users\Hp\PycharmProjects\python_training\5.file handling\normal_file_handling")

# "counting the no of lines in the file"

# "Counter class"

from collections import Counter
# path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\text files\sindhu.txt"
# with open(path) as file:
#     l = []
#     for line in file:
#         if line.strip():
#             list_ = line.split()
#             for word in list_:
#                 l.append(word)
#
# word = Counter(l)
# print(word)
# print(Counter.most_common(word))
# string_ = 'python is a language'
# dict_count = Counter(string_)
# for item in dict_count:
#     print(item, dict_count[item])

from itertools import islice
# string_ = "python"
# print(*list(islice(string_,0,3)))

"print first n lines in file"
# path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\text files\sindhu.txt"
# with open(path) as file:
#     res = islice(file, 2)
#     print(list(res))

"to print a particular series of lines"
path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\text files\sindhu.txt"
# # with open(path) as file:
# #     res = islice(file, 3,5)
#     print(*list(res))

"to print last n lines"
# using islice
n = 3
# with open(path) as file:
#     for lineno,line in enumerate(file):
#         pass
#     file.seek(0)
#     print(lineno-2)
#     res = islice(file,lineno-2, lineno)
#     print(list(res))

"using deque"
from collections import deque
# with open(path) as file:
#     res = deque(file, 3)
#     print(list(res))

"to print last 5 lines in a file"
n = 5
# with open(path) as file:
#     res = deque(file, n)
#     print(list(res))

"to print first n linses"
n = 4
# with open(path) as file:
#     res = islice(file, n)
#     print(*(list(res)))

"reading and writing into a file (using only single context manager)"
path_r = r"C:\Users\Hp\PycharmProjects\python_training\my_files\text files\sindhu.txt"
path_w = r"C:\Users\Hp\PycharmProjects\python_training\my_files\text files\sindhu12.txt"
# with open(path_r) as file_r, open(path_w, 'a') as file_w:
#     file_w.write(file_r.read())
#     # file_w.write(file_r.read())
#     file_w.writelines(file_r.readlines())

"csv file"
import os
import csv
# print(os.getcwd())
with open("bio.csv",'w') as csv_file:
    write_obj = csv.writer(csv_file)
    write_obj.writerow({'name','gender','mobile'})
    write_obj.writerows({('mohanakasi','male','8886213059')}) # it takes int format also
# os.popen("temp.csv")
# with open("bio.csv") as csv_file:
#     read_obj = csv.reader(csv_file)
#     for row in read_obj:
#         print(row)

# with open("bio.csv") as csv_file:
#     read_obj = csv.DictReader(csv_file)
#     # print(next(read_obj))
#     for row in read_obj:
#         if row['gender'] == 'female':
#             print(row['name'])

with open("write.csv",'w') as csv_file:
    write_obj = csv.DictWriter(csv_file,['x','y','z'])
    write_obj.writeheader()
    write_obj.writerow({'x':20, 'y':30, })

import csv
import json
from collections import defaultdict
"""inc csv files each line in the file is considered as a row"""
path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\kasi.csv"

"file reading"
# with open(path,'r') as csv_file:
#     read_obj = csv.reader(csv_file)
#     for row in read_obj: # reads each row as a list
#         print(row)

"""while reading using csv.reader() each row is in type of list"""
"""and each elemet in that list is a string"""

path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\csv_files\sample.csv"
# with open(path) as csv_file:
    # r_obj = csv.reader(csv_file)
    # for row in r_obj:
    #     # print(type(row))
    #     for element in row:
    #         print(type(element))
"""file reader using Dict Reader"""
"""while reading throuth DictReder each row is a dictionary"""
"""each elekment in that is a type string(key or value)"""
path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\csv_files\sample.csv"
# with open(path) as csv_file:
#     r_obj = csv.DictReader(csv_file)
#     for row in r_obj:
#         # print(type(row))
#         for element in row:
#             # print(element) # keys
#             # print(type(element)) # each key is a type string
#             print(row[element]) # values
#             print(type(row[element])) # each value is of type string
"file reading (using dictionary method)"
# with open(path,'r') as csv_file:
#     read_obj = csv.DictReader(csv_file)
#     print(read_obj)
#     for row in read_obj:  # reads each row as a dictionary and key will be header (first row eleme)
#         print(row)


# "file writing"
# with open(path,'w') as csv_:
#     write_obj = csv.writer(csv_)
#     write_obj.writerow(['x','y','z'])
#     write_obj.writerows([('kasi','rao','mohan'),('a','b','c')])
#
# "file reading (using dictionary method)"
# "file writing"
# with open(path,'w') as csv_:
#     dictwriter_obj = csv.DictWriter(csv_.writer(["x","y","z"]))

"""write a program to read all the employees in employee table"""
path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\csv_files\employees.csv"
# with open(path) as csv_file:
#     read_obj = csv.reader(csv_file)
#     next(read_obj)
#     for row in read_obj:
#         if row:
#             print(row[0])


"""write program to print only the names with salaries > 7000"""
# with open(path) as csv_file:
#     read_obj = csv.reader(csv_file)
#     next(read_obj)
#     for row in read_obj:
#         if int(row[-1]) > 7000:
#             print(row[0])


"""wap to group male and female names""" "(using default dict)"
# with open(path) as csv_file:
#     dd = defaultdict(list)
#     read_obj = csv.reader(csv_file)
#     next(read_obj)
#     for row in read_obj:
#         dd[row[1]] += [row[0]]
#     print(dd)

"""wap to gropu employees based on their temas"""
# with open(path) as csv_file:
#     dd = defaultdict(list)
#     read_obj = csv.reader(csv_file)
#     next(read_obj)
#     for row in read_obj:
#         if row:  # if any row is empty it wil raise error so that we have to check if empty or not
#             dd[row[2]] += [row[0]]   # row.strip() will wont work because row is not a string for that we directly taken row in if
#     print(dd)  # so if row empty the condition give false else if data is there in row it gives true

"""sort the shares in tes.csv file based on the share prices"""
path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\csv_files\test.csv"
# with open(path) as csv_file:
#     read_obj = csv.DictReader(csv_file)
#     l = list(read_obj)
#     res = sorted(l, key = lambda d: float(d['price']))
#     print(list(res))

"""writer a program to add alll the shares in test.scv file"""
# with open(path) as csv_file:
#     add = 0
#     read_obj = csv.DictReader(csv_file)
#     for row in read_obj:
#         add += float(row['price'])
#     print(add)

"""write operation csv_files"""
"""writerow"""
"""write row takes one list as anargment and in the list elements can be of any data type"""

"""writerows"""
"""write rows take an iterable conatinging multiple iterables and it will write each iterable inside an iterable as a row into file"""

"""using dcv.writer()"""
"""while writing using csv.writer the list contains any data type"""
import csv
path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\csv_files\sample.csv"
with open(path,'w') as csv_file:
    write_obj = csv.writer(csv_file)
    write_obj.writerow(['name','age','sal'])
    write_obj.writerow(['m kasi',25,'3000'])
    write_obj.writerow(['rao','48','284000'])
    write_obj.writerows((('kasi',25,25000),['mohana',20,'10000']))

"""using DictWriter"""
"""while writing through csv.DictWriter the keys must be of type string and values a=of any data type"""
with open(path, 'a') as csv_file:
    w_obj = csv.DictWriter(csv_file, ['name','age','sal'])
    w_obj.writeheader()
    w_obj.writerow({'name':'robo', 'age':25, 'sal':78121})
    w_obj.writerow({'name':'kasi','sal':4592, 'age':74})
    w_obj.writerows([{'name':'rao','sal':2500000, 'age': 8900},{'name':'viswa','age':47,'sal':4000}])
"""writing using writerows() that contains a iterable of multiple dictionaries while write through DictWriter"""




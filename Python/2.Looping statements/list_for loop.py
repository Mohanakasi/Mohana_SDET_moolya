'''' traversing through list'''''
list_ = [1,2,3,'kasi']
for item in list_:
    print(item)

''""""program for travesrsing through list uisng enumerate"""''
# list_ = ['laptop', 'pen', 'mobile']
# for index,item in enumerate(list_):
#     print(index,item)


""" travesrsing reverse through list uisng reversed class"""
# list_ = ['laptop', 'pen', 'mobile']
# for item in reversed(list_):
#     print(item)

"""travesrsing reverse through list"""
# list_ = ['laptop', 'pen', 'mobile']
# res = []
# for item in list_:
#     res = [item]+res
# print(res)

"""travesrsing reverse through list"""
# list_ = ['laptop', 'pen', 'mobile']
# for index in range(-1,-(len(list_)+1),-1):
#     print(list_[index],end = ' ')


""" program to print alternate items in a list (even) """
# list_ = ['kasi','nadh',0,12,3]
# for index in range(0,len(list_),2):
#     print(list_[index],end = ' ')

""" to print alternate items in a list (odd) """
# list_ = ['kasi','nadh',0,12,3]
# for index in range(1,len(list_),2):
#     print(list_[index],end = ' ')
#

""" to print alternate items in a list  (even) """
# list_ = ['kasi','nadh',0,12,3]
# for index in range(len(list_)):
#     if index % 2 == 0 :
#         print(list_[index], end=' ')

""" program to print only numbers in a list using inbuilt method"""
# list_ = ['kasi','jmr',2020]
# for item in list_:
#     if isinstance(item,int):
#         print(item)


"""checking numerical values in a list (int,float,complex)"""""
# list_ = ['kasi','jmr',2020,2.0,50+50j]
# for item in list_:
#     if isinstance(item,(int,float,complex)):
#         print(item , end = ' ')

""" print item in list with it's length"""
# list_ = ['kasi','python','bangalore','2021','2022']
# for item in list_:
#     print((item,'....>',len(item)))


"""print even length items in a list"""
# list_ = ['kasi','python','bangalore','123456','2021','2022']
# for item in list_:
#     if len(item) % 2 == 0:
#         print(item,end = ' ')


"""print even length items in a list using inbuilt function"""
# list_ = ['kasi','python','bangalore','123456','2021','2022']
# list2_ = []
# for item in list_:
#     if len(item) % 2 == 0:
#         list2_.append(item)
# print(list2_)

""" print even length items in a list without using inbuilt function"""
# list_ = ['kasi','python','bangalore','123456','2021','2022']
# list2_ = []
# for item in list_:
#     if len(item) % 2 == 0:
#         list2_ += [item]
# print(list2_)

"""print even length items in a list without using inbuilt function"""
# list_ = ['kasi','python','bangalore','123456','2021','2022']
# list2_ = []
# for item in list_:
#     if len(item) % 2 == 0:
#         list2_ += [item]
# print(list2_)
#     new_ = input("enter the new string into the list")
#     list2_.insert(1,new_)
# pritn(list2_)

"""printing if item in a string is even lenth as is it is , if it is odd length reverse the item
(creating a new lst) """
# list_ = ['kasi','from',guntur','@','2021','to',bangalore','2022']
# list2_ = []
# for item in list_:
#     if len(item) % 2 == 0:
#         list2_.append(item)
#     else:
#         list2_.append(item[::-1])
# print(list2_)

"""printing if item in a string is even lenth as is it is , if it is odd length reverse the item 
(modifing original list)"""
# list_ = ['kasi','from','guntur','2021','to','bangalore','2022']
# for index in range(len(list_)):
#     if len(list_[index]) % 2 == 0:
#         continue
#     else:
#         list_[index] = list_[index] [::-1]
# print(list_)

"""write a program to modify the exisitng list if item is of type string reverse it else keep it as it is
(modifying original list)"""
# list_ = ['kasi','guntur',1008,536,1.85,50+50j,('jmr'),{4253},[85,'mohana'],{'a':52,'b':25200},'python','knows']
# for index in range(len(list_)):
#     if isinstance(list_[index],str):
#         list_[index] = list_[index] [::-1]
#     else:
#         list_[index] = list_[index]
# print(list_)


"""write a program to modify the exisitng list if item is of type string reverse it else keep it as it is
(creating new listlist)"""
# list_ = ['kasi','guntur',1008,536,1.85,50+50j,('jmr'),{4253},[85,'mohana'],{'a':52,'b':25200},'python','knows']
# list2_ =[]
# for item in list_:
#     if isinstance(item,str):
#         list2_.append(item[::-1])
#     else:
#         list2_.append(item)
# print(list2_)

"""print the strings in a list which are starting with vowels"""
# list_ = ['kasi', 'is', 'from','ernakulam']
# for item in list_:
#     if isinstance(item,str) and (item[0].lower() in 'aeiou'):
#         print(item)


"""wap to print all the extensions in a list"""
# list_ = ['youtube.txt','gmail.com','kasi.py','python.exe']
# for item in list_:
#     a = item.split('.')
#     print(a[-1])


"""wap to print all the file names in a list if file is of odd length"""
# list_ = ['youtube.txt','gmail.com','kasi.py','python.exe']
# for item in list_:
#     a = item.split('.')
#     if (len(a[0]) % 2 !=0 ):
#         print(a[0], end = ' ')

"""wap to print all the file names in a list if file is of odd length (using unpacking)"""
# list_ = ['youtube.txt','gmail.com','kasi.py','python.exe']
# for item in list_:
#     filename,extension = item.split('.')
#     if (len(filename) % 2 !=0 ):
#         print(filename, end = ' ')


"""checking index of first occurence of a nimber in list (using inbuilt method)"""
# list_ = [20,30,10,50,20,10]
# list2_ = []
# num = 10
# index = 0
# for item in list_:
#     if (num==item) and (item not in list2_):
#         list2_ += [item]
#         index = list_.index(item)
# print(index)

"""checking index of first occurence of a number in list (without suing nbuilt method)"""
# list_ = [20,30,10,50,20,10]
# num = 10
# for item,index in enumerate(list_):
#     if num == item:
#         print(f"the index of {num} is {index}")
#         break
#     else:
#         print("number not present in list")

"""prime number"""
# n = 5
# for i in range(2,n):
#     if n % i == 0:
#         print("not a prime number")
#         break
# else:
#     print("prime number")



"""series of prime numbers"""
# n = 10
# for item in range(n+1):
#     if item>1:
#         for i in range(2,item):
#             if item % i == 0:
#                 break
#         else:
#             print(f"{item} is a prime number")

"""kipping a particular value in a list"""
# list_ = [10,20,30,40,50,60]
# num = 50
# for item in list_:
#     if num == item:
#         continue
#     print(item)

"""printing palindrome in a list"""
# n = ['kasi','malayalam','dad','mom',8008,1001]
# for item in n:
#     value = str(item)
#     if value == value[::-1]:
#         print(f"{value} is a palindrome")


"""if item in a list is string keep it as it is else reverse that item"""

# list_ = ['kais',1.0,True,[1,4,56]]
# res = []
# for item in list_:
#     if isinstance(item,str):
#         res += [item]
#     elif isinstance(item,(list,tuple,set,dict)):
#         res += [item[::-1]]
#     else:
#         res += [str(item)[::-1]]
# print(res)

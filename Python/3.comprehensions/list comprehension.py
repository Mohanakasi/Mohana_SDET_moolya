''"""print list having powers of each element of another list"""''
"""(normal method)"""
# list_ = [1,2,3,4]
# res  = []
# for item in list_:
#     res.append(item**2)
# print(res)

"""(using list comprehension)"""
# list_ = [1,2,3,4]
# res = [item**2 for item in list_]
# print(res)



"""to print a list having tuple of index and item of another list normal method"""
"""(normal method)"""
# list_ = [1,2,3,4]
# res  = []
# for index,item in enumerate(list_):
#     res += [(index,item)]
# print(res)

"""(using list comprehension)"""
# list_ = [1,2,3,4]
# res = [(index,item) for index,item in enumerate(list_)]
# print(res)

"""creating list of even no's using list comprehension"""
# list_ = list(range(10))
# res = [ item for item in list_ if item %2 == 0]
# print(res)


"""creating lists of even and odd using list comprehension"""
# list_ = list(range(10))
# even = [ item for item in list_ if item % 2 == 0  ]
# odd = [ item for item in list_ if item % 2 != 0]
# print(even)
# print(odd)

"""   if word is of even append into list as it is if word lenth is odd reverser it """
"""(using normal method)"""
# list_ = ['kasi' , 'jmr', 'mohana' , '123']
# res = []
# for item in list_:
#     if len(item) % 2 == 0:
#         res += [item]
#     else:
#         res += [item[::-1]]
# print(res)

"""using list comprehension"""
# list_ = ['kasi' , 'jmr', 'mohana' , '123']
# res = [item if len(item) % 2 == 0 else item[::-1] for item in list_]
# print(res)


"""if item in a list is string keep it as it is else reverse that item"""
"""normal method"""
# list_ = ['kais',1.0,True,[1,4,56]]
# res = []
# for item in list_:
#     if isinstance(item,str):
#         res += [item]
#     else:
#         res += [str(item)[::-1]]
# print(res)

"""(using list comprehension)"""
# list_ = ['kais',1.0,True,[1,4,56]]
# res = [item[::-1] if isinstance(item,str) else item for item in list_]
# print(res)

"""create a list having words starting with owel (using list comprehension)"""
# list_ = ['kasi', 'User', 'Imr','iam']
# res = [item for item in list_ if item[0].lower() in 'aeiou']
# print(res)


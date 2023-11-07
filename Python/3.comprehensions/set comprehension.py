""""""" set comprehension to create a set of squares from 1 to 10"""""""
# res = {item**2 for item in range(1,11)}
# print(res)


"""tuple of index and item using enumewrate"""
# list_ = ['ksi','jmr',1,2,3]
# res = {item for item in enumerate(list_)}
# print(res)
#
# list_ = ['ksi','jmr',1,2,3]
# res = {(index,list_[index]) for index in range(len(list_))}
# print(res)

"""use set comprehension  to create a set of tuples having item and it's index pair of list using range()"""
# list_ = ['ksi','jmr']
# res = {(list_[index],len(list_[index]))  for index in range(len(list_))}
# print(res)
#
"""use set comprehension  to create a set of tuples having item and it's lenth pair of list using enumerate()"""
# list_ = ['ksi','jmr']
# res = {(item,len(item)) for index,item in enumerate(list_) }
# print(res)



"""use set comprehension  to create a set of tuples having item and it's lenth pair of list using range()"""
# list_ = ['ksi','jmr']
# res = {(list_[index],len(list_[index])) for index in range(len(list_))}
# print(res)


"""set comprehension to create a set with even items present in a list"""
# list_ = [1,2,3,4,80,55,380,4520]
# res = {item for item in list_ if item % 2 == 0}
# print(res)



"""set comprehension to create a set with even items present in a list (unsing range())"""
# list_ = [1,2,3,4,80,55,380,4520]
# res = {list_[index] for index in range(len(list_)) if list_[index] % 2 == 0}
# print(res)



"""set comprehension to create a set with even items present in a list (using enumwereate)"""
# list_ = [1,2,3,4,80,55,380,4520]
# res = {item for index,item in enumerate(list_) if item % 2 == 0 }
# print(res)

"""set comprehension to create a set with if the item has even length keep it as its else reverse it"""
# list_ = ['kasi', 'jmr','i','iam']
# res = {item if len(item) % 2 == 0 else item[::-1] for item in list_}
# print(res)



"""set comprehension to create a set with if the item has even length keep it as its else reverse it (using range)"""
# list_ = ['kasi', 'jmr','i','iam']
# res = {list_[index] if len(list_[index]) % 2 ==0 else list_[index][::-1] for index in range(len(list_)) }
# print(res)

# set comprehension to create a set with if the item string  keep it as its else reverse it
# list_ = ['kasi', 'jmr',1,2,3,True]
# res  = {item if isinstance(item,str) else str(item)[::-1] for item in list_}
# print(res)

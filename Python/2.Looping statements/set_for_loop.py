''"""traversing through set"""''
set_ = {'kasi',1008,1,2,3}
for item in set_:
    print(item)

"""removing a particular element in a set"""
set_ = {1,2,3,4}
value = 3
for item in set_:  '''this program will get error because we cant remove the element using for loop because as it'''
    if item == value:   '''is unordered if we the remove the item size of the set again changes in middle'''
        set_.discard(item)
print(set_)


""" remove the element from the set  """

set_ = {"python", "dad", "hai", "malayalam", "madam", "mom"}
key = "hai"

for ele in set_:  """using break only possible to remoove the item in a set"""
    if ele == key:
        set_.discard(key)
        break

print(set_)

"""adding items into a set  if the  item is a palindrome"""
list_ = ['kasi','malayalam','dad','mom']
set_ = set()
for item in list_:
    if item == item[::-1]:
        set_.add(item)
print(set_)


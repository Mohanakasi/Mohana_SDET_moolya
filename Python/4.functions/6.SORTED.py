"""INTRO"""
"""**********************sorted inbuilt-function***********************"""
"""returns a new sorterd list from the items in the iterable"""
"""iterable was ther mandatory arguments for the sorted"""
"""key and reverse are the optional keword arguments"""
"""key specifies a function of one argument that is used to extract compariosn key from each element in the iterable"""
"""reverse is a boolean value, by default it is set to to False"""
"""if reverse is set to True all the items in the iterable becomes reversed"""

"""write a program to sort the strings in the list based on their length"""
list_ = ['kasi','is','from','guntur','he','learning','python']
res = sorted(list_, key = len)
# print(res)

"reverse= True"
res = sorted(list_, key = len, reverse=True)
# print(res)

"""write a program to find the largest and shortest word in the given string"""
sentence = 'python has powerful oops'
res = sorted(sentence.split(), key = len)
# print(f"longest word--->{res[-1]}, shortest word--->{res[0]}")

"""write a program to find the largest and shortest words along with their lengths in the given string"""
sentence = 'python has powerful oops'
res = sorted(sentence.split(), key = len)
# print(f"longest word--->{(res[-1], len(res[-1]))}, shortest word--->{(res[0], len(res[0]))}")

"""write a program to sort the below list elements based on the last charazcter of each string"""
list_ = ['bag','jmr','guntur','pepper','deodrant','bench','and','kasi']
sort_list = sorted(list_, key = lambda string:string[-1])
# print(sort_list)

"""write a program to sort the below list based on first character of each string"""
list_ = ['bag','jmr','guntur','pepper','deodrant','bench','and','kasi']
sort_list = sorted(list_, key = lambda string:string[0])
# print(sort_list)


"""sort the below ditionary based keys ascii values"""
d = {'apple':100, 'kasi':1995, 'jmr':1995, 'robo':2019}
# print(sorted(d))  # if we give dictionary without key it will sorted based on key;s ascii values implicitly
# print(sorted(d.keys())) # using inbuilt
res = sorted(d.items(), key = lambda item:item[0])
# print(dict(res)) # printing dictionary after sorting

"""sort the below dictionay based on values (values is of type int or string any one only)"""
d = {'a':80, 'z':40, 'j':18, 'robo':2}
# print(sorted(d, key = lambda key_:d[key_]))  # sorts based values and returns a list of keys
# print(sorted(d.values())) # using inbuilt (# sorts based values and returns a list of values)
res = sorted(d.items(), key = lambda item:item[-1])
# print(dict(res))

"""sort the below ditionary based keys length"""
d = {'apple':100, 'kasi':1995, 'jmr':1995, 'robo':2019}
# print(sorted(d, key = len))
# print(sorted(d.keys(), key = len))
res = sorted(d.items(), key = lambda item:item[0]) # returns a loist of tuples each tuple having key and value
# print(dict(res))

"""sort the dictionary based on keys last character"""
dict_ = {'location':'bangalore', 'course':'python', 'doj': '10-08-2021','place':'basavanagudi'}
res = sorted(dict_.items(), key = lambda item:item[0][-1])
print(dict(res))

"""write a program to get the most repeted word in the string (by using dictionary comprehension and sorted function)"""
string_ = 'hai hello kasi how is hai python is python is python oops is king'
words = string_.split()
dict_ = {word:words.count(word) for word in words}
res = sorted(dict_.items(), key = lambda item:item[-1])
print(res[-1][0])

"""write a program to print longest word with it's length (by using dictionary comprehension and sorted function)"""
string_ = 'hai hello mohanakasi how is hai python is python is python oops is king'
words = string_.split()
dict_ = {word: len(word) for word in words}
res = sorted(dict_.items(), key = lambda item:item[-1])
print(f"{res[-1][0]}, length--->{res[-1][-1]}")

"""write a program to print longest non repeted word (by using dictionary comprehension and sorted function)"""
string_ = 'hai hello mohanakasi how is hai python is python is python oops is kingofandghra'
words = string_.split()
dict_ = {word: len(word) for word in words if words.count(word) == 1 }
res = sorted(dict_.items(), key = lambda item:item[-1])
print(res[-1][0])



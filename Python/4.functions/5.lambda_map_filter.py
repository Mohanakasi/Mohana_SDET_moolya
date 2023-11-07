"intro lambda function"
"""any anonymous function that defined without name is called as lambda function"""
"""after creating lambda function you have to strore it in a variable and we have to call that variable by passing argments"""
"""in lambda function we can take n number of arguments"""
"""but expression is only one to take"""
"""and only one single---->if is not acceptable in lambda function"""
"""if we want to take if in lambda function we have to take else block also"""
"""we can take and, or logical operators in a single expression"""
"""pass break continue kewords are not used in lambda function"""
"""we can take collection (one or any no of) as argument  to the lambda function but expression is one only"""
"""we cant do looping in lambda functions"""
"""to achieve looping we use map and filter functions along with the lambda fuctions"""

"""write a lambda expression that checks the given no is even or not"""
res = lambda n: n%2 == 0
# print(res(98))
"""write a lambda expression that multiplies two numbers"""
multi_two = lambda n1,n2: n1*n2
# print(multi_two(100,200))

"""write a lambda expression that return last elemts of the sequence"""
las_ele_seq = lambda seque:seque[-1]
# print(las_ele_seq('kasi'))
# print(las_ele_seq([1,2,'jmr']))
# print(las_ele_seq((1,89,'mohana kasi')))

"""write a lambda function that checks if the string is palindrome or not"""
pal_check = lambda string_: string_ == string_[::-1]

# print(pal_check('kasi'))
# print(pal_check('malayalam'))

"""lambda expression to check string is a palindrome and to print it if it is a palindrome"""
pal_ = lambda string_: string_ if string_ == string_[::-1] else None
# print(pal_('kasi'))
# print(pal_('dad'))
# print(pal_('mom'))

"""write a lambda express that print's whether the the number is even or odd"""
ev_odd = lambda num: "even" if num % 2 == 0 else "odd"
# print(ev_odd(8))
# print(ev_odd(456))
# print(ev_odd(123))

"""lambda expression to check string is of even length and string stars with vowel"""
ev_l_vow = lambda string_: len(string_) % 2 == 0 and string_[0].lower() in 'aeiou'
# print(ev_l_vow("user"))


"""we cant do looping in lambda functions"""
"""to achieve looping we use map and filter functions along with the lambda fuctions"""

"""***************************map**********************************"""
"""map function applies a function to all the items in the iterable"""
"""map takes a function and iterable as an arguments"""
"""in map we can have n no of iterables but the no of iterables must match with the parameters in the function definition"""
"""if the multiple iterables are of different length data loss will occurs"""
"""in the function we must use return statement for result"""
"""if we takes only one if block in function the map will implicitly returns none for the false results"""
"""after completion of map function we have take it into a variable and type cast it (to list tuple or set only) """

"""wap to convert all the strings in the list to upper case using map"""
def upper_(string_):
    return string_.upper()

list_ = ['kasi','jmr','mohan kasi','guntur','vrdl']
conv_string_upper = map(upper_, list_)
# print(list(conv_string_upper))

"""wap to convert all the strings in the list to lower case using map"""
def upper_(string_):
    return string_.lower()

list_ = ['KASI', 'JMR', 'MOHAN KASI', 'GUNTUR', 'VRDL']
conv_string_upper = map(upper_, list_)
# print(list(conv_string_upper))

"""using lambda"""
list_ = ['KASI', 'JMR', 'MOHAN KASI', 'GUNTUR', 'VRDL']
conv_string_upper = map(lambda item: item.upper(), list_)
# print(list(conv_string_upper))

"""wap to convert allthe negeative numbers into positive using map"""
def pos_(item):
    return abs(item)

list_ = [-10,-25,-45]
neg_pos_con = map(pos_, list_)
# print(list(neg_pos_con))

"""using lambda"""
list_ = [-10,-25,-45]
neg_pos_con = map(lambda item: abs(item), list_)
# print(list(neg_pos_con))

"""write a map function that return a list of even numbers inside a list using map"""
def ev_odd(item):
    if item % 2 == 0:
        return item

l = [10,7,4,5,6,456]
res = map(ev_odd,l)
# print(list(res))

"""taking tuple as an iterable"""
def ev_odd(item):
    if item % 2 == 0:
        return item

l = (10,7,4,5,6,456)
# res = map(ev_odd,l)
# print(list(res))

"""write a map function that takes two lists and return sum of each elements\n"""
"""(sum of first index item of 1ist1   with first index item of list2 .....)"""
from itertools import zip_longest
def ev_odd(item1,item2):
    return item1 + item2

l = [10,7,4,5,6,456]
l1 = [78,56,45]
# res = map(ev_odd,l,l1)
# print(list(res))

'''write a map function that returns lenth of the each string present inside the list, tuple, set, and dictionary '''
def len_(item):
    return len(item)
my_name = ['mohana kasi','jmr','kasi']
l_str_ite = map(len_, my_name)
# print(list(l_str_ite))

"""using lambda"""
my_name = ['mohana kasi','jmr','kasi']
l_str_ite = map(lambda string_: len(string_), my_name)
# print(list(l_str_ite))

"""using dictionary as an iterable"""
def len_(item):
    if isinstance(item, str):
        return len(my_name[item])
my_name = {'a':'mohana kasi', 'b':'visweswara rao', 'c':'settipalli'}
# l_str_ite = map(len_, my_name)
# print(list(l_str_ite))


"""using lambda"""
my_name = {'a':'mohana kasi', 'b':'visweswara rao', 'c':'settipalli'}
l_str_ite = map(lambda key: len(my_name[key]), my_name)
# print(list(l_str_ite))



'''write a map function that returns the  numeric data present  inside the list, tuple, set, and dictionary '''
def numeric_(item):
    if isinstance(item, (int, float, complex)):
        return item

num_iter = map(numeric_, ['kasi',50+50j,1008,'jmr',2020])
# print(list(num_iter))

"""write a map function that returns the strings having even lenth present inside a list"""
def ev_le_str(item):
    if isinstance(item, str):
        if len(item) % 2 == 0:
            return item

l = ['kasi','python','bangalore','test yanthra']
ev_list = map(ev_le_str, l)
# print(list(ev_list))

""""write a map function to create a dictionary of word and it's count pair in the following sentence"""
def dict_(word):
    return word, words.count(word)

sentence = 'kasi is in banagalore, kasi knows python'
words = sentence.split()
wor_count_dict = map(dict_, words)
# print(dict(wor_count_dict))

"""using lambda"""
sentence = 'kasi is in banagalore, kasi knows python'
words = sentence.split()
wor_count_dict = map(lambda word: (word,words.count(word)), words)
# print(dict(wor_count_dict))


""""write a map function to return the words starting with vowels"""
def vow_words(word):
    if word[0].lower() in 'aeiou':
        return word

l = ['kasi','rao','user','id','internals','externals','jaya']
list_vow_words = map(vow_words, l)
# print(list(list_vow_words))

""""write a map function to return the palindrome strings inside a list"""
def pal_(string_):
    if string_ == string_[::-1]:
        return string_

l = ['kasi','malayalam','mohana','dad']
pal_words = map(pal_, l)
# print(list(pal_words))

"""write a map function that returns the list of numbers raised to the power of their indices using map"""
"""we cant directly unpack the items in the argument position of lambda function"""
def powers(item):
    index, num = item
    return num ** index

l = [45,8,2,32,12,9]
num_p = map(powers, list(enumerate(l)) )
# print(list(num_pow))


"""using lampda"""
l = [45,8,2,32,12,9]
num_pow = map(lambda item: item[1]**item[0], list(enumerate(l)) )
# print(list(num_pow))

"""write a map function that returns all the words in lower case in the given sentence"""
sentence = 'KASI Is In BANGALORE'
words_low = map(lambda word: word.lower(), sentence.split())
# print(list(words_low))

"""**********************************filter()***************************"""
"""the filter function takes a function and an iterable as an argument"""
"""it provides an elegant way to filter out all the elements of a sequence for which the function returns true"""
"""filter creates a list of elements for which a function returns true"""
"""filter takes only one iterable as an argument """
"""filter passes each element in the iterable through the function and returns elements which was true"""
"""if we given any expression after return statement it doesn't execute that"""

"""filter out the even values in the list"""
def even(item):
    if item % 2 == 0:
        return item

l = [8,7,9,45,6,7]
ev_values = filter(even, l)
# print(list(ev_values))

"""using lambda function"""
l = [8,7,9,45,6,7]
ev_values = filter(lambda item:item % 2 == 0, l)
# print(list(ev_values))


"""write a program that returns a list of strings with odd length using filter function"""
def len_string_(string_):
    if len(string_) % 2 !=0:
        # return string_[::-1] # it avoides expression given in return statement
        return string_
l = ['kasi','userid','mohana kasi','is','python','bangalore']
od_strings = filter(len_string_, l)
# print(list(od_strings))

"""using lambda function"""

# print(list(filter(lambda item:item[0].lower() in 'aeiou',['attributes','user id','mohana kasi','elegant','iam kasi'])))

"""write a function that return a list of only even numbers inside a list using filter()"""
def ev_check(num):
    if num % 2 == 0:
        return num

l = [1008,1006,420,806,8,59,45]
ev_list_num = filter(ev_check, l)
# print(list(ev_list_num))


"""using lambda"""
l = [1008,1006,420,806,8,59,45]
ev_list_num = filter(lambda num: num % 2 ==0, l)
# print(list(ev_list_num))

'''write a function that returns only the  numeric data present  inside the list, tuple, set, and dictionary '''
def numeric_check(item):
    if isinstance(item, (int, float, complex)):
        return item

l = ['kasi',1008,8.923,50+50j,2020,2021,1,'visweswara rao','jmr',2022]
# numeric_list = filter(numeric_check, l)
# print(list(numeric_list))

"""using lambda function"""
l = ['kasi',1008,8.923,50+50j,2020,2021,1,'visweswara rao','jmr',2022]
numeric_list = filter(lambda item: isinstance(item, (int, complex, float)), l)
print(list(numeric_list))

"""write a  function that returns only the strings which having even lenth present inside a list"""
def temp(string_):
    if len(string_) % 2 == 0:
        return string_


list_ = ['user','mohana','python','bangalore','coninuity']
even_len_strings = filter(temp,list_)
# print(list(even_len_strings))

"""using lambda function"""
list_ = ['user','mohana','python','bangalore','coninuity']
even_len_strings = filter(lambda item: len(item) % 2 == 0,list_)
# print(list(even_len_strings))

""""write a function to returns only the words starting with vowels"""
def vo_wors(word):
    if word[0].lower() in 'aeiou':
        return word

sentence = "filter takes only one iterable"
string_vowel = filter(vo_wors, sentence.split())
# print(list(string_vowel))

"""using lambda function"""
sentence = "filter takes only one iterable"
vowels = filter(lambda word: word[0].lower() in 'aeiou', sentence.split())
# print(list(vowels))

"""write a function to returns only the palindrome strings inside a list"""
def pal_check(string_):
    if string_ == string_[::-1]:
        return string_

list_ = ['malayalam','isi','imi','jmr','dad','kasi']
pal_strs = filter(pal_check, list_)
# print(list(pal_strs))

"""using lambda function"""
list_ = ['malayalam','isi','imi','jmr','dad','kasi']
pal_strs = filter(lambda string_: string_ == string_[::-1], list_)
# print(list(pal_strs))

"""write a function that returns only the lowercase words in the given sentence"""
def case_check(word):
    if word.islower():
        return word

sentence = 'PYTHON is a oops language'
low_words = filter(case_check, sentence.split())
# print(list(low_words))

"""using lambda function"""
sentence = 'PYTHON is a oops language'
low_words = filter(lambda word: word.islower(), sentence.split())
# print(list(low_words))






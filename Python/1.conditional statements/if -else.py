""""""
""" WAP to check if the given input number is even or odd"""
# number = 3
#
# if number % 2 == 0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd number")


""" WAP to check if the character is lowercase or uppercase"""

# char = "r"

# if "a" <= char <= "z":
#     print(f"{char} is lowercase")
#
# else:
#     if "A" <= char <= "Z":
#         print(f"{char} is uppercase")
#     else:
#         print(f"{char} is not an alphabet")


#####################################################

# char = "r"
# if "a" <= char <= "z":
#     print(f"{char} is lowercase")
#
# elif "A" <= char <= "Z":
#     print(f"{char} is uppercase")
#
# else:
#     print(f"{char} is not an alphabet")






"""checking the element is present in tupple"""
# col_=("kasi",1008,'jmr')
# element = 'jmr'
# if element in col_:
#     print("the element {} is present in collection {}".format(element,col_))
# else:
#     print("the element is not present in collection")


'''checking if character is a alphabet or number or special character'''
# char = input("enter the character")
# if 'a'<=char<='z':
#      print("the character is in lower case")
# elif 'A'<=char<='z':
#     print("the char is in upper case")
# else:
#     print("the char is special character")


'''chech wheter iterable is empty or not'''
# iterable='hello'
# if iterable:
#     print("not empty")
# else:
#     print("empty")


'''converting character to lower and lowe to upper'''
# char='h'
# if 'a'<=char<='z':
#     print(chr(ord(char)-32))
# elif 'A'<=char<='Z':
#     print(chr(ord(char)+32))
# else:
#     print(char)



'''converting character to lower and lowe to upper only using inbuilt methods'''
# char='H'
# if char.isupper():
#     lowe_char=char.lower()
#     print(lowe_char)
# elif char.islower():
#     upper_char=char.upper()
#     print(upper_char)
# else:
#     print("char is a special symbol")



'''checking string starts with vowel'''
# string = 'wam '
# if (string[0] in 'aeiouAEIOU'):
#     print("string starting with Vowel")
# else:
#     print("string not start with vowel")


'''checking string ends with vowel'''
# string = 'KAsi'
# if string[-1] in "aeiouAEIOU":
#     print("string ends with vowel")
# else:
#     print("string not ends with vowel")


'''checking integer is palindrome'''
# num = 8008
# string_ = str(num)
# if string_ == string_[::-1]:
#     print("palindrome")
# else:
#     print('not a palindrome')


'''checking iterable contains even or odd no of elements'''
# iterable_ = ['kasi', 1008, 'jmr']
# if len(iterable_) %2 == 0:
#     print(len(iterable_))
#     print(f"{iterable_} contains even no of elements")
# else:
#     print(f"{iterable_} contains odd no of elements")


'''checking if the number has first digit as even or odd'''
# num = 3486
# string_ = str(num)
# a = int(string_[0])
# if a % 2 == 0:
#     print(f" {num} contains first digit as even")
# else:
#     print(f" {num} contains first digit as odd")

'''checking if the number has first digit as even or odd (using inline if- else)'''
# num = 1234
# string_=str(num)
# a=int(string_[0])
# print("even" if a % 2 == 0 else "odd")

'''checking the character is a vowel or not'''
# char = 'a'
# dictionary_ = {}
# if char in 'aeiouAEIOU':
#     dictionary_[char] = ord(char)
#     print(a={dictionary_)
#
# else:
#     print(f"the {char} is not a vowel")


'''finding greatest of three numbers'''
# a = 103000000000000000000000000000000000000
# b = 10600000000000000000000000000000000
# c = 108000000000000000000000000000000000000
# if (a>b) and (a>c):
#     print("a is greater")
# elif b>a and b>c :
#     print(" b is greater")
# elif c>a and c>b:
#     print(" c is greater")
# else:
#     print("any of two are same")


'''marks evaluation'''
# marks = int(input("enter the marks"))
# if 0 <= marks < 35:
#     print("fail")
# elif 35 <= marks <= 60:
#     print("second class")
# elif 61 <= marks <= 75:
#     print("first class")
# elif 76 <= marks <= 100:
#     print("distinction")
# else:
#     print("enter valid marks")



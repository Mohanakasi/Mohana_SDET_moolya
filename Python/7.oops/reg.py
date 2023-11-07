import re
"find all"
"matches the sub string or character and returns a list"


"matchina a series or a particular characters"
print(re.findall('[aeiou]','hai hello world')) # matching vowels in the string
print(re.findall('[012345]','hai hello world chandana@420'))
print(re.findall('[0-5]','hai hello world chandana@42089'))
print(re.findall('[0-9]','hai hello world chandana@9')) # matches numbers in the string
print(re.findall('[a-z]','Hello KASI How are yiu')) #matches lower case alphabets only
print(re.findall('[A-Z]','Hello KASI How are yiu')) # matches upper cases alphabets only
print(re.findall('[A-Za-z]','Hello KASI How are yiu')) # matches both the lower and upper cases letters

"matching numbers, alphabets(lower&upper)"
print(re.findall('[0-9A-Za-z]','Hello KASI How are yiu')) # matches the numbers lower and upper cases letters
"or"
print(re.findall('\w','Hello KASI _How are yiu')) # matches the numbers, lower and upper cases letters and '_'

"matching only special characters"
print(re.findall('[^0-9A-Za-z]','Hello K&&ASI How are yiu')) # matches the special characters only
"or"
print(re.findall('\W','Hello K&&ASI')) # matches the special characters only


"[]+"
"gives  you entire sub string matched in between the range given"
print(re.findall('[0-9]+','Hello KASI your registration no is 1008'))
print(re.findall('[A-Z]+','KASI how are yiu'))

"\d equivalent to [0-9]"
print(re.findall('\d','Hello KASI How are yiu 8886213059'))
print(re.findall('\d+','Hello KASI How are yiu 8886213059'))

"\s matches with the white spaces in the given string"
print(re.findall('\s','kasi kasi kasi lol')) # matches only white spaces

print(re.findall('\S','kasi kasi kasi lol')) # matches all apart from white spaces
print(re.findall('\S+','kasi kasi kasi lol')) # matches all apart from white spaces(gives you whole words)



"^ inside a starting of the character set"
"nothing but negation"
print(re.findall('[^0-9]','Hello KASI 8886213059')) # it will avoid numbers and matches individual alphabets
"or"
print(re.findall('\D','Hello KASI 8886213059')) # it will avoid numbers and matches individual alphabets

print(re.findall('[^0-9]+','Hello Kasi 8886213059')) # it will avoid numbers and matches whole words
"or"
print(re.findall('\d+','Hello KASI 8886213059 and 090')) # it will avoid numbers and matches individual alphabets
print(re.findall('\d{6}','Hello KASI  560001 and 8886213059 and 090'))

"word boundary"
"transition between non word to word at front & word to non word transition at back side of the substring\n" \
"then it is called as word boundary"

"matching 6 numbers"
print(re.findall(r'\b[0-9]{6}\b','560001 is a 09 country '))

print(re.findall(r'\b\w{2}\b','560001 is a 09 country '))

"matching two upper alphabets"
print(re.findall(r'\b[A-Z]{2}\b','560001 IS a 09 country  A CVOU'))

print(re.findall(r'\b[A-Z]{2,4}\b','560001 IS a 09 country  MOHANA A CVOU')) # {2,4} means mini 2 max 4

print(re.findall(r'\bh\w*\b','hai hello a h aksi'))  # '\bh\w*\b' means starts with h and later 0 or any-->(*)

print(re.findall(r'\b\w+h\b','hai helo h strength'))  # '\bh\w+\b' means starts with h and later 0 or any-->(*)

"""adding numbers in a string"""
print(re.findall(r'\d','hai helo h 12,strength78'))

"sum of individual numbers in a string using regular expresssions"
total = 0
for item in re.findall(r'\d','hai helo h 12,strength78'):
    total += int(item)
print(total)

"sum of multiple numbers in a string using regular expressions"
total = 0
for item in re.findall(r'\d+','hai helo h 12,strength78'):
    total += int(item)
print(total)

"to find total spaces in a string using regular expressions"
total = []
for item in re.findall(r'\s','hai helo h 12,strength78'):
    total.append(item)
print(f" total spaces in string is {len(total)}")



"to count the number of occurences of each non special characters (only alphabets)"
"usinng default dict"
from collections import defaultdict
dd = defaultdict(int)
total = []
for item in re.findall(r'[A-za-z]','hai helo h 12,strength78'):
    dd[item] += 1
print(dd)

"using dictionary comprehension"
letters = re.findall(r'[A-za-z]','hai helo h 12,strength78')
d = {item:letters.count(item) for item in letters}
print(d)


"count the characters in each word and ignore special characters"
words = re.findall(r"\b[A-Za-z0-9]+\b", 'hai12 opi7 _issegsdgdsgo*&')
for item in words:
    print(item, len(item))

"count the upper case characters in string using regular expressions"
res = [char for char in re.findall(r"[A-Z]", 'Hai Hello  KASI How125Po^%%')]
print(len(res))


"finding valid phone numbers from a list"
l = ['123-4567-890', '888-621-3059']
for word in l:
    match = re.findall(r"\d{3}-\d{3}-\d{4}", word)
    if match:
        print(match)
    else:
        print(f"not valid phone number--->{word}")

"finding phone numbers startiwith 8 or 9 followed by 00 ex(800 or 900)"
l = ['123-4567-890', '800-621-3059', '901-789-4568','900-745-3214']
for word in l:
    match = re.findall(r"[89]00-\d{3}-\d{4}", word) # [89] means either 8 or 9
    if match:
        print(f"reqired one -----> {match}")
    else:
        print(f"not requird number -----> {word}")


"finding vowel words in a list"
l = ['iam', 'king', 'user']
# for word in l:
#     match = re.findall(r"\b[aeiou]\w+\b", word) # [aeiou]\w+ ---> it will check characters only so take it i
#     if match:
#         print(match)

"finding consonents words in a list"
l = ['iam', 'king', 'user']
for word in l:
    match = re.findall(r"\b[^aeiou\s]\w+\b", word) # [aeiou]\w+ ---> it will check characters only so take it i
    if match:
        print(match)

"finding three letter words in list"
l = ['iam', 'king', 'user', 'rcb', 'Mumbai']
for word in l:
    match = re.findall(r"\b\w{3}\b", word)
    if match:
        print(match)
    else:
        print(f"{word} is Not a 3 letter word")









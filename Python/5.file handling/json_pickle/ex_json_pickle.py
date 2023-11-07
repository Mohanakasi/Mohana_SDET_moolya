"""json"""
import json
import pickle
"""dumps & loads"""

"""dumps"""
"""serialize any python object into json formatted string"""
"""serializing python object"""
string_ = 'kasi learning python'
res = json.dumps(string_)
# print(type(res))

"""de-serializing"""
"""loads"""
"""loads de serializes any json formatted string into python objects"""
de_ser = json.loads(res)
# print(de_ser)
# print(type(de_ser))


import json
path = r"C:\Users\Hp\PycharmProjects\python_training\my_files\text files\sample.txt"
msg = ['hello python\n','hai kasi\n']
sal = [20,80]
with open(path,'w') as file:
    json.dump(msg, file)
    # json.dump(sal,file)
with open(path) as file:
    print(json.load(file))


"""pickle files"""
import pickle
l = {'name':'kasi', 'age':25}
with open(path,'wb') as file:
    res = pickle.dump(l,file)
with open(path,'rb') as file:
    res = pickle.load(file)
    print(type(res))





# import pickle
# string_ = {'a':1007}
# res = pickle.dumps(string_)
# print(type(res))
# d_ser = pickle.loads(res)
# print(type(d_ser))


"""json in files"""
"""writing python objects into file using json"""
path =r"C:\Users\Hp\PycharmProjects\python_training\my_files\text files\sample.txt"
import json
# with open


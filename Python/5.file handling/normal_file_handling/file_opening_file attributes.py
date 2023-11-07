import os
from collections import *

# when we want to open a file we can acces it by passing file name as argument if you waorking #
# in same directory or else copy path of the file where the file is present and place in a variable using rawstrings
# and use that path variable inside the open() if you specifies the read mode it will be in read mode or it will
# implicitly open as a read mode


"opening a file"
"""without context manager"""
file = open("temp.csv")
os.chdir(r"C:\Users\Hp\PycharmProjects\python_training\my_files")
print("currect directory","------>",os.getcwd())
print("file name","------>",file.name)
print("file mode","------>",file.mode)
print(file.readable())
print(file.writable())
os.chdir(r"C:\Users\Hp\PycharmProjects\python_training\file handling\file handling")
os.popen("sindhu12.txt")
print(list(file))
print(os.path.exists("../../my_files/text files/sindhu12.txt"))
print(os.path.getsize("../../my_files/text files/sindhu12.txt"))

"""using context manager"""
os.chdir(r"C:\Users\Hp\PycharmProjects\python_training\my_files")
with open("sindhu.txt", 'r') as file:
    print(file.name) # prints file current opened file name
    print(file.readable()) #   # prints true if file is readable
    print(file.writable()) # prints true if file is writable
    print(file.mode)      # prints current mode
    print(file.closed) #  prints True if file is closed
    print(file.close()) # closes the file


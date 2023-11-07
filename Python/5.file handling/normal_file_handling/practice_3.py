"print even numbers present inside a list"
def ev_odd(l):
    for i in l:
        if i % 2 == 0:
            print(i)

# ev_odd([48,56,98])

"traverse through string using function"
# def trav(string):
#     for char in string:
#         print(char)
#
# trav('kasi')

"traverse sthrough dictionary using functions"
# def trav(**kwargs):
#     for key in kwargs:
#         print(key)
#
# trav(a=10, b=20)



# "print char and it's index in a string"

#
# class father:
#     def __init__(self, fname, mname, lname='settipalli'):
#         self.fname = fname
#         self.mname = mname
#         self.lname = lname
#
#     def get_data(self):
#         print(self.__dict__)
#
#
# p1 = father('p','kondaiah')
# p1.get_data()
#
# class mother(father):
#
# p2 = mother('venkata','lakshmi')
# p2.get_data()
#
# class child(father):

# p3 = child('mohana kasi','visweswara rao')
# p3.get_data()

"to count the no of special characters in a string"
def sp_ch(string):
    for char in string:
        if not (char.isalpha() or char.isdigit()):
            print(char)

sp_ch('kasi&%$&*(%$Y&*%$')
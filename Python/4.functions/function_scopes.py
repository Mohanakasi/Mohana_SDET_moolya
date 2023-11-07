# a = 10
# def func():
#     print(a)
#     a += 1  # error
#
# func()


"""global key word"""
# a = 10
# def func():
#     global a
#     a += 5
#     print(a)
#
# func()
# print(a)



"""non local kry word"""
a = 10
def f1(): # main function
    x = 10
    def f2():  # nedted function
        nonlocal x # to modify the non local variable inside the nested function we have to make use
                    # non local key word
        x += 5
        print(x)
    f2()
f1()
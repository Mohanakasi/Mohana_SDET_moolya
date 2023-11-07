def in_(func): # func = cd
    print(func)
    def cu(*args, **kwargs):
        print(func)
        print("some_c1")
        func(*args, **kwargs)
        # print(func)
        print("some_c1_1")
    return cu

def inn_(func): # func = a
    print(func)
    @in_  #cd = in_(cd) # op-->cu
    def cd(*args, **kwargs):
        print("more")
        func(*args, **kwargs)
    # print(cd)
    # print(cu)
    return cd # returnning cu
@in_ # c = in_(c)
@inn_ # a = inn_(a) a = cu
def a(b):
    print(b)
a("hai") # a nothing but cu
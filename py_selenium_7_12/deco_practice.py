import time


def wait_deco(func): #func --> add_nums
    def wrapper(*args, **kwars):
        time.sleep(10)
        print("iam the extra functionality")
        return func(*args, **kwars)
    return wrapper

@wait_deco #add_nums = wait_deco(add_nums) wrapper
def add_nums(a, b):
    return a+b

print(add_nums(10, 40))

"decorate some functions with some time delay"
import time
l = [1,8,9,]
def delay(func):
    def wraper(*args, **kwargs):
        time.sleep(5)
        return func(*args, **kwargs)
    return wraper

@delay
def ev_length_word(string_):
    for word in string_.split():
        if len(word) % 2 == 0:
            print(word, "--->", len(word))

ev_length_word('this is called python')

@delay
def string_upper(string_):
    return string_.upper()

print(string_upper('lopill'))
# default arguments = A default value for certain parameters default is used when that argument
#                     is omitted make your functions more flexible, reduces no. of arguments
#                     1. Positional, 2.DEFAULT, 3.Keyword, 4.Arbitrary

import time

def counter(start, end):
    for d in range(start, end+10):
        print(d)
        time.sleep(0.2)
    print("OK, Baby!")
counter(0,1000)

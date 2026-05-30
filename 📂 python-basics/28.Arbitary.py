# *args = allows you to pass multiple non-key arguments (for tuple)
# **kwargs = allows you to pass multiple keyword-arguments (for dict)
#           * unpacking operator
#           1.positional 2.default 3.keyword 4.ARBITRARY

# Using this * sign if you want to use countless number of arguments in your function without
#   mentioning then it can be used like this:

def multi(*nums):
    count = 0
    for num in nums:
        count += num
    return  count
print(multi(10,12,15,58,69))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("My","name","is","Pritam") # by this *args keyword you can unpack how many arguments you wanna use
print()

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value,end=" ")

    print(f"{kwargs.get('City')}")
    print(f"{kwargs.get('resident')} {kwargs.get('State')}")

shipping_label("Mr.","Nichole","Doe",
               resident="123 Baker Street",
               City="Paris",
               State="Hoover") #following the args then you can mention kwargs as if you mention kwargs first it will show error.


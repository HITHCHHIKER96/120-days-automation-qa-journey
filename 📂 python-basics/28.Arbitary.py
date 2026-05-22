# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
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

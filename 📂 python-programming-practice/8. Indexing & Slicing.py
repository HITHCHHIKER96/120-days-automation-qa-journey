#indexing = accessing elements of a sequence using [] (indexing operator, [start:end:step])

# String indexing allows you to access individual characters using positive (0-based) or negative (-1 from end) indices
# String slicing uses [start:end:step] syntax to extract substrings, with start inclusive and end exclusive
# Negative indexing provides convenient access to characters from the end of strings using negative numbers
# Step slicing with [::step] enables advanced operations like reversing strings ([::-1]) and skipping characters

my_list = ['apple', 'banana', 'cherry', 'date']
# Normal Indexing
print(my_list[0:])
print(my_list[1:3])
print(my_list[:2])
# Negative Indexing
print(my_list[-1])
# Step
print(my_list[::3]) #it will count every third character

# Reverse the list
print(my_list[::-1])

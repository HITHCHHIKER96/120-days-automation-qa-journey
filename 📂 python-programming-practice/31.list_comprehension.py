# List Comprehension = A concise way to create lists in Python.
#                       Compact and easier way to read that traditional loops
#                        [expression for value n iterable if condition]
#Python list comprehensions provide a concise, one-line syntax to create new lists from existing iterables.
#They are typically cleaner and execute faster than traditional for loops.
doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1,30)]
squares = [z * z for z in range (1,20)]

print(doubles)

# new_list = [expression for item in iterable]
#Expression: The operation or modification applied to each element.
# Item: The temporary variable tracking the current element.
# Iterable: The source collection (e.g., list, string, range, tuple).

even = [x for x in range(20) if x % 2 == 0]
print(even)

numbers = [1, 2, 3, 5, 9]
positive_nums = [num for num in numbers if num >= 0]
print(positive_nums)

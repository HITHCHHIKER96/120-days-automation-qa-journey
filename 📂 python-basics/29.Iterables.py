#Iterables = An object/collection that can return its element one at a time,
            # allowing it to be iterated over in a loop.

#1. Standard Sequence Iteration (Lists, Tuples, Strings)
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a string
word = "Python"
for letter in word:
    print(letter)

#Dictionary Iteration
user = {"name": "Alice", "role": "Admin", "id": 404}

# Iterate over keys (default)
for key in user:
    print(key)

# Iterate over values
for value in user.values():
    print(value)

# Iterate over key-value pairs (items)
for key, value in user.items():
    print(f"{key}: {value}")

#Behind the Scenes: How Iterables Work
numbers = [10, 20]

# Manually mimicking a for loop
my_iterator = iter(numbers)

print(next(my_iterator))  # Output: 10
print(next(my_iterator))  # Output: 20
# print(next(my_iterator)) # This would raise StopIteration exception


my_dict ={"A":1, "B": 2, "C": 3, "D":4, "E":5}
for x in my_dict.values():
    print(x)

for key, value in my_dict.items():
    print(f"{key} = {value}")  #by this you can print both value and key

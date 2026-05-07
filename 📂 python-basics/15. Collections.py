# collection = single "variable" used to store multiple values
# List = [] ordered and changeable.
# Set = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuples = () ordered and unchangeable. Duplicates OK. FASTER.

cars = ["Hyundai", "Suzuki", "Honda", "TATA"]

for car in cars:
    print(cars) # when you print this it will print like this
# ['Hyundai', 'Suzuki', 'Honda', 'TATA']
# ['Hyundai', 'Suzuki', 'Honda', 'TATA']
# ['Hyundai', 'Suzuki', 'Honda', 'TATA']
# ['Hyundai', 'Suzuki', 'Honda', 'TATA']
# What happens:
#
# Loop runs 4 times (one for each car)
# Each time, print(cars) prints the whole list
    # print(car) # when you print this it will only run one time.
    # print(dir(cars)) # this is a method(dir()) by which we can know that how many methods this list can perform
    # print(help(cars)) # and by this you can get description of each these methods
    # print("bmw" in cars) # byt his in operator you can find the value is present or not in the list

# There are bunch-of methods of lists
fruits = ['apple', 'banana', 'cherry']

fruits[1] = 'blueberry'     # Change element
fruits.append('date')        # Add to end
fruits.insert(1, 'avocado')  # Insert at position
fruits.remove('cherry')      # Remove by value
removed = fruits.pop(0)      # Remove by index (returns it)
del fruits[0]                # Delete by index
print(fruits)

# In set we cannot use index methods as it is immutable
# Tuples are faster than Lists

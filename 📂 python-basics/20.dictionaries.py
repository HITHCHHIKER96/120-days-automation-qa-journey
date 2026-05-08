# Dictionaries = a collection of {key:value} pairs
#                ordered and changeable. No duplicates
# Dictionaries is same as sets
country_creation = {"Hyundai" : "South Korea",
                    "Suzuki": "Japan",
                    "BMW": "Germany",
                    "Toyota": "Japan"
                    }
print(dir(country_creation)) # this dir() function can show that how many methods and attributes are there in dictionaries,
# not only dictionaries but in all collection

# Commonly Used Methods
# Method		Description
# .keys()		Returns a view object of all keys in the dictionary.
# .values()		Returns a view object of all values.
# .items()		Returns all key-value pairs as tuples.
# .update()		Merges another dictionary or iterable into the current one.
# .clear()		Removes all items from the dictionary.
# 	Iterating Through a DictionaryYou can loop through different parts of a dictionary using a for loop:
# Looping through keys: for key in my_dict:
# Looping through values: for val in my_dict.values():
# Looping through both: for key, val in my_dict.items():

# Modules: a file containing code -including functions, classes, and
#          variables—saved with a .py extension you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files.

# print(help("modules"))

# Types of Modules:
"""
Built-in Modules: Pre-installed libraries bundled with Python like math, sys, os, and random.
User-Defined Modules: Custom .py files you create to organize your own codebase.
Third-Party Modules: External libraries installed via pip from the Python Package Index (PyPI) such as pandas or requests.

1. Import the Entire Module
Imports everything and preserves the module namespace.
You access its elements using dot notation

"""
# Eg:
import math
print(math.sqrt(2))

"""
2. Import Specific Attributes
Brings only specific functions or variables directly into your file so you can bypass the module name prefix.

"""
#Eg:
from math import sqrt, pi
print(sqrt(987))
print(pi)

"""
3. Import with an AliasShortens a module's name using the as keyword to make your code cleaner.

"""
#Eg:
import random as rd
print(rd.randint(1,30))

"""
4. Import it into another file (e.g., main.py) located in the same directory:python# main.py
Create the module file (e.g., calculator.py):python# calculator.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
    
import calculator

result = calculator.add(10, 5)
print(result)  # Output: 15

"""

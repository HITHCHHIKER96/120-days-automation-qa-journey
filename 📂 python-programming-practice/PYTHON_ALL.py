# 🐍 Python Programming — From Zero to Hero
### A Complete 20-Chapter Course | Inspired by Bro Code

---

> **Who is this for?** Absolute beginners to intermediate learners who want to master Python step-by-step through clear explanations, code examples, and hands-on projects.

---

## 📚 Table of Contents

| Chapter | Topic |
|---------|-------|
| [Chapter 1](#chapter-1--introduction-to-python) | Introduction to Python |
| [Chapter 2](#chapter-2--variables--data-types) | Variables & Data Types |
| [Chapter 3](#chapter-3--type-casting--user-input) | Type Casting & User Input |
| [Chapter 4](#chapter-4--strings--string-methods) | Strings & String Methods |
| [Chapter 5](#chapter-5--math-operators--numbers) | Math, Operators & Numbers |
| [Chapter 6](#chapter-6--if-statements--conditionals) | If Statements & Conditionals |
| [Chapter 7](#chapter-7--loops) | Loops |
| [Chapter 8](#chapter-8--functions) | Functions |
| [Chapter 9](#chapter-9--lists) | Lists |
| [Chapter 10](#chapter-10--tuples-sets--dictionaries) | Tuples, Sets & Dictionaries |
| [Chapter 11](#chapter-11--lambda-map-filter--reduce) | Lambda, Map, Filter & Reduce |
| [Chapter 12](#chapter-12--object-oriented-programming--classes) | OOP — Classes & Objects |
| [Chapter 13](#chapter-13--inheritance--polymorphism) | Inheritance & Polymorphism |
| [Chapter 14](#chapter-14--magic-methods--properties) | Magic Methods & Properties |
| [Chapter 15](#chapter-15--exception-handling) | Exception Handling |
| [Chapter 16](#chapter-16--file-handling) | File Handling |
| [Chapter 17](#chapter-17--modules-packages--standard-library) | Modules, Packages & Standard Library |
| [Chapter 18](#chapter-18--decorators--generators) | Decorators & Generators |
| [Chapter 19](#chapter-19--multithreading--apis) | Multithreading & APIs |
| [Chapter 20](#chapter-20--gui-development--final-projects) | GUI Development & Final Projects |

---

## Chapter 1 — Introduction to Python

### 1.1 What is Python?

Python is a high-level, interpreted, general-purpose programming language created by **Guido van Rossum** in 1991. It is designed to be easy to read and write, making it an ideal first language for beginners.

> 🌟 **Why Python?** Python is used in web development, data science, AI/ML, automation, game development, scripting, and cybersecurity. It is consistently ranked as one of the **top 3 most popular programming languages** in the world.

### 1.2 Python Features

- ✅ Simple & readable syntax — almost like writing English
- ✅ Interpreted — runs line by line, no compilation step
- ✅ Dynamically typed — no need to declare variable types
- ✅ Multi-paradigm — Object-Oriented, Procedural, and Functional
- ✅ Huge standard library — "batteries included"
- ✅ Cross-platform — runs on Windows, Mac, Linux
- ✅ Free and Open Source

### 1.3 Installing Python

1. Go to **[python.org](https://python.org)** and download the latest version (3.x)
2. Run the installer — ⚠️ **Check "Add Python to PATH"** before clicking Install Now
3. Verify in your terminal:

```bash
python --version
# Python 3.12.0
```

### 1.4 Choosing an IDE

| IDE / Editor | Best For |
|---|---|
| PyCharm Community | Beginners — full Python IDE, free |
| VS Code + Python Extension | Lightweight, highly customizable |
| Thonny | Absolute beginners, very simple |
| Jupyter Notebook | Data Science, interactive coding |
| IDLE | Comes with Python, very basic |

### 1.5 Your First Python Program

```python
# hello.py — My First Python Program

print("Hello, World!")
print("Welcome to Python!")
print("Let's start coding!")
```

**Output:**
```
Hello, World!
Welcome to Python!
Let's start coding!
```

> 📝 **Note:** `print()` displays output to the console. Strings must be in quotes. `#` starts a comment — ignored by Python.

### 1.6 How Python Works

Python is **interpreted** — the Python interpreter reads and executes your `.py` file line by line. Source code is compiled to **bytecode** (`.pyc`) and executed by the **Python Virtual Machine (PVM)**.

---

## Chapter 2 — Variables & Data Types

### 2.1 What is a Variable?

A variable is a **named container** that stores a value in memory. In Python, you create a variable by assigning a value using `=`. No type declaration needed!

```python
name       = 'Alice'
age        = 25
gpa        = 3.85
is_student = True

print(name)        # Alice
print(age)         # 25
print(gpa)         # 3.85
print(is_student)  # True
```

### 2.2 The 4 Core Data Types

| Data Type | Example Values |
|---|---|
| `str` (String) | `"Hello"` `'Python'` `"123"` |
| `int` (Integer) | `10` `-5` `0` `1000` |
| `float` (Decimal) | `3.14` `-0.5` `9.99` `2.0` |
| `bool` (Boolean) | `True` / `False` |

### 2.3 Checking the Type

```python
name     = 'Bro'
age      = 21
height   = 5.11
is_cool  = True

print(type(name))     # <class 'str'>
print(type(age))      # <class 'int'>
print(type(height))   # <class 'float'>
print(type(is_cool))  # <class 'bool'>
```

### 2.4 Naming Rules for Variables

- Must start with a **letter** or **underscore** (`_`)
- Cannot start with a number
- Can contain letters, numbers, and underscores
- **Case-sensitive** — `name` and `Name` are different
- Cannot use Python reserved keywords (`if`, `for`, `while`, etc.)

```python
# ✅ VALID
my_name  = 'Alice'
_age     = 25
price2   = 9.99

# ❌ INVALID
# 2name = 'Bob'   ← starts with number
# my-var = 5      ← hyphens not allowed
# for = 10        ← reserved keyword
```

### 2.5 Multiple Assignment

```python
# Same value to multiple variables
x = y = z = 0

# Multiple values in one line
name, age, city = 'Alice', 25, 'Delhi'
print(name)  # Alice
print(age)   # 25
print(city)  # Delhi
```

### 2.6 Constants (Convention)

```python
# Use ALL_CAPS to indicate a value should not change
PI       = 3.14159
MAX_SIZE = 100
WEBSITE  = 'python.org'
```

> 💡 **Tip:** Python uses `snake_case` for variable names — this is the official **PEP 8** style guide convention.

---

## Chapter 3 — Type Casting & User Input

### 3.1 Type Casting

| Function | Converts To |
|---|---|
| `int(x)` | Integer (whole number) |
| `float(x)` | Float (decimal number) |
| `str(x)` | String (text) |
| `bool(x)` | Boolean (True / False) |

```python
x = 3.99
print(int(x))       # 3  (truncates, does NOT round)

y = 10
print(float(y))     # 10.0

z = 3.14
print(str(z))       # '3.14'

# bool() — Truthy and Falsy values
print(bool(1))      # True
print(bool(0))      # False
print(bool('hi'))   # True
print(bool(''))     # False  ← empty string = False
print(bool(None))   # False
```

### 3.2 Accepting User Input

`input()` always returns a **string** — cast it if you need a number!

```python
# Basic input
name = input('What is your name? ')
print('Hello, ' + name + '!')

# Numeric input — must cast!
age   = int(input('Enter your age: '))
price = float(input('Enter price: '))
print(f'You are {age} years old. Price is ${price}')
```

> ⚠️ **Warning:** If the user types `abc` when you expect a number, `int()` will raise a `ValueError`. Always validate input (covered in Chapter 15).

### 3.3 Mini Project — Rectangle Area Calculator

```python
print('=== Rectangle Area Calculator ===')

length = float(input('Enter length: '))
width  = float(input('Enter width: '))

area      = length * width
perimeter = 2 * (length + width)

print(f'Area      = {area}')
print(f'Perimeter = {perimeter}')
```

### 3.4 Mini Project — Shopping Cart

```python
print('=== Shopping Cart ===')

item     = input('Item name: ')
price    = float(input('Price per unit: $'))
quantity = int(input('Quantity: '))
tax_rate = 0.08

subtotal = price * quantity
tax      = subtotal * tax_rate
total    = subtotal + tax

print(f'\nItem:     {item}')
print(f'Subtotal: ${subtotal:.2f}')
print(f'Tax:      ${tax:.2f}')
print(f'Total:    ${total:.2f}')
```

---

## Chapter 4 — Strings & String Methods

### 4.1 String Basics

```python
s1 = 'Hello'
s2 = "World"
s3 = '''This is a
multi-line string'''

# Concatenation
greeting = s1 + ' ' + s2
print(greeting)    # Hello World

# Repetition
print('Ha' * 3)    # HaHaHa
```

### 4.2 F-Strings (Formatted String Literals)

```python
name = 'Alice'
age  = 25
gpa  = 3.856

print(f'Name: {name}')
print(f'Age: {age}')
print(f'GPA: {gpa:.2f}')          # 2 decimal places → 3.86
print(f'{name} is {age} years old')
print(f'2 + 2 = {2 + 2}')         # Expressions work!
```

### 4.3 String Indexing & Slicing

```python
text = 'Python'
#      0 1 2 3 4 5    (positive index)
#     -6-5-4-3-2-1    (negative index)

print(text[0])      # P
print(text[-1])     # n  (last character)
print(text[1:4])    # yth
print(text[:3])     # Pyt
print(text[3:])     # hon
print(text[::-1])   # nohtyP  (reversed!)
```

### 4.4 Common String Methods

Case Transformation

These methods adjust the capitalization of characters within a string. [1]
capitalize(): Converts the first character to uppercase and the rest to lowercase.
lower(): Converts all characters to lowercase.
upper(): Converts all characters to uppercase.
title(): Converts the first character of each word to uppercase.
swapcase(): Swaps uppercase to lowercase and vice versa.
asefold(): A stronger version of lower() used for case-insensitive comparisons (e.g., handles special characters like the German "ß"). [1, 2, 3, 4, 5, 6]

Searching and Finding
Methods for locating specific characters or substrings.
find(sub[, start[, end]]): Returns the lowest index where the substring is found, or -1 if not found.
rfind(sub[, start[, end]]): Returns the highest index (last occurrence) of the substring.
index(sub[, start[, end]]): Like find(), but raises a ValueError if the substring isn't found.
rindex(sub[, start[, end]]): Like rfind(), but raises a ValueError if the substring isn't found.
count(sub[, start[, end]]): Returns the number of non-overlapping occurrences of a substring. [1, 2, 3]

Splitting and Joining
Essential for breaking strings into lists or merging items into a single string. [1, 2, 3]
split(sep=None, maxsplit=-1): Splits a string into a list based on a delimiter (defaults to whitespace).
rsplit(sep=None, maxsplit=-1): Splits a string from the right.
join(iterable): Concatenates elements of an iterable (like a list) using the string as a separator.
partition(sep): Splits the string at the first occurrence of sep and returns a 3-tuple.
rpartition(sep): Splits the string at the last occurrence of sep and returns a 3-tuple.
splitlines([keepends]): Splits the string at line breaks. [1, 2, 3, 4]

Trimming and Padding
strip([chars]): Removes leading and trailing characters (defaults to whitespace).
lstrip([chars]): Removes leading characters.
rstrip([chars]): Removes trailing characters.
center(width[, fillchar]): Returns a centered string of a specified width.
ljust(width[, fillchar]): Left-justifies the string.
rjust(width[, fillchar]): Right-justifies the string.
zfill(width): Pads the string with zeros on the left until it reaches the specified width. [1, 2, 3, 4, 5]

Boolean Checks
These return True or False based on string content. [1, 2, 3]
startswith(prefix[, start[, end]]): Checks if the string starts with a specific value.
endswith(suffix[, start[, end]]): Checks if the string ends with a specific value.
isalnum(): True if all characters are alphanumeric.
isalpha(): True if all characters are alphabetic.
isdecimal() / isdigit() / isnumeric(): Check for various types of numeric characters.
islower() / isupper(): Checks if characters are in a specific case.
isspace(): True if the string consists only of whitespace.
isprintable(): True if all characters are printable.
isidentifier(): True if the string is a valid Python identifier. [1, 2, 3, 4]

Formatting and Modification
replace(old, new[, count]): Replaces occurrences of old with new.
**format(*args, kwargs): Formats values into a template string.
removeprefix(prefix): Removes a specific prefix if it exists (Python 3.9+).
removesuffix(suffix): Removes a specific suffix if it exists (Python 3.9+).
expandtabs(tabsize=8): Replaces tab characters with a specified number of spaces.
encode(encoding='utf-8', errors='strict'): Returns an encoded version of the string as bytes.
translate(table): Returns a copy of the string where each character is mapped through the given translation table.
maketrans(x[, y[, z]]): Static method that creates a translation table for translate().



| Method | Example & Result |
|---|---|
| `.upper()` | `'hello'.upper()` → `'HELLO'` |
| `.lower()` | `'HELLO'.lower()` → `'hello'` |
| `.strip()` | `'  hi  '.strip()` → `'hi'` |
| `.replace(a, b)` | `'cat'.replace('c','b')` → `'bat'` |
| `.split(sep)` | `'a,b,c'.split(',')` → `['a','b','c']` |
| `.find(sub)` | `'hello'.find('l')` → `2` |
| `.count(sub)` | `'banana'.count('a')` → `3` |
| `.startswith()` | `'Python'.startswith('Py')` → `True` |
| `.endswith()` | `'code.py'.endswith('.py')` → `True` |
| `.isdigit()` | `'123'.isdigit()` → `True` |
| `.isalpha()` | `'abc'.isalpha()` → `True` |
| `.title()` | `'hello world'.title()` → `'Hello World'` |
| `.join(list)` | `', '.join(['a','b','c'])` → `'a, b, c'` |

```python
# Practical example
email = '  USER@EXAMPLE.COM  '
clean = email.strip().lower()
print(clean)   # user@example.com

csv_data = 'Alice,25,Delhi'
name, age, city = csv_data.split(',')
print(f'{name} is {age} from {city}')
```

> 💡 **Tip:** Strings are **immutable** — methods return NEW strings. Always save the result: `name = name.upper()`

---

## Chapter 5 — Math, Operators & Numbers

### 5.1 Arithmetic Operators

| Operator | Example & Result |
|---|---|
| `+` Addition | `5 + 3` → `8` |
| `-` Subtraction | `10 - 4` → `6` |
| `*` Multiplication | `3 * 4` → `12` |
| `/` Division | `10 / 3` → `3.333...` (always float) |
| `//` Floor Division | `10 // 3` → `3` (integer result) |
| `%` Modulus | `10 % 3` → `1` (remainder) |
| `**` Exponentiation | `2 ** 8` → `256` |

```python
# Order of operations (PEMDAS applies)
result = 2 + 3 * 4      # 14  (not 20)
result = (2 + 3) * 4    # 20

# Modulus tricks
print(10 % 2 == 0)      # True  → even number
print(7  % 2 == 1)      # True  → odd number

# Augmented assignment
x = 10
x += 5    # 15
x -= 3    # 12
x *= 2    # 24
x //= 5   # 4
```

### 5.2 The `math` Module

```python
import math

print(math.pi)           # 3.141592653589793
print(math.sqrt(144))    # 12.0
print(math.ceil(4.1))    # 5  (round up)
print(math.floor(4.9))   # 4  (round down)
print(math.pow(2, 10))   # 1024.0
print(math.factorial(5)) # 120
print(math.gcd(12, 8))   # 4
print(math.sin(math.pi / 2))  # 1.0
```

### 5.3 Built-in Math Functions

```python
print(abs(-42))           # 42
print(round(3.14159, 2))  # 3.14
print(max(1, 5, 3, 9))    # 9
print(min(1, 5, 3, 9))    # 1
print(sum([1, 2, 3, 4]))  # 10
print(pow(2, 8))           # 256
```

### 5.4 Random Numbers

```python
import random

print(random.random())            # Float: 0.0 to 1.0
print(random.randint(1, 6))       # Int: 1 to 6 (dice roll!)
print(random.uniform(1.0, 10.0))  # Float in range

colors = ['red', 'green', 'blue']
print(random.choice(colors))      # Random element
random.shuffle(colors)            # Shuffle in place
```

---

## Chapter 6 — If Statements & Conditionals

### 6.1 The `if` Statement

Python uses **indentation** (4 spaces) to define code blocks — not curly braces!

```python
age = 18

if age >= 18:
    print('You are an adult.')
    print('You can vote!')

print('This always runs.')  # Outside the if block
```

### 6.2 if / elif / else

```python
score = 75

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f'Your grade is: {grade}')
```

### 6.3 Comparison & Logical Operators

| Operator | Meaning & Example |
|---|---|
| `==` | Equal to: `5 == 5` → `True` |
| `!=` | Not equal to: `5 != 3` → `True` |
| `<` | Less than: `3 < 5` → `True` |
| `>` | Greater than: `5 > 3` → `True` |
| `<=` | Less or equal: `5 <= 5` → `True` |
| `>=` | Greater or equal: `6 >= 5` → `True` |
| `and` | Both must be True: `age > 18 and has_id` |
| `or` | At least one True: `is_admin or is_mod` |
| `not` | Inverts boolean: `not False` → `True` |

```python
age    = 20
has_id = True

if age >= 18 and has_id:
    print('Entry allowed')

# Membership operators
fruits = ['apple', 'banana', 'cherry']
if 'banana' in fruits:
    print('Banana is in the list!')

if 'mango' not in fruits:
    print('Mango is NOT in the list')
```

### 6.4 Ternary (Conditional) Expression

```python
# Syntax: value_if_true  if  condition  else  value_if_false

age    = 20
status = 'Adult' if age >= 18 else 'Minor'
print(status)   # Adult

num    = 7
parity = 'Even' if num % 2 == 0 else 'Odd'
print(parity)   # Odd
```

### 6.5 Nested `if` Statements

```python
temperature = 35
is_raining  = False

if temperature > 30:
    if is_raining:
        print('Hot and rainy — take an umbrella!')
    else:
        print('Hot and sunny — wear sunscreen!')
else:
    print('Nice weather today!')
```

---

## Chapter 7 — Loops

### 7.1 `while` Loop

```python
# Basic while loop
count = 1
while count <= 5:
    print(f'Count: {count}')
    count += 1   # IMPORTANT: always update the variable!

# Countdown
n = 10
while n >= 0:
    print(n)
    n -= 1
print('Blast off!')
```

### 7.2 Input Validation with `while`

```python
while True:
    age = int(input('Enter your age (0-120): '))
    if 0 <= age <= 120:
        break             # Exit the loop
    else:
        print('Invalid! Try again.')

print(f'Your age is {age}')
```

### 7.3 `for` Loop

```python
# Looping over a range
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 11, 2):   # 0, 2, 4, 6, 8, 10 (step=2)
    print(i)

for i in range(10, 0, -1):  # 10, 9, 8 ... 1 (countdown)
    print(i)
```

### 7.4 Iterating Over Collections

```python
# Iterate over a string
for char in 'Python':
    print(char)     # P y t h o n

# Iterate over a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# enumerate — get index AND value
for index, fruit in enumerate(fruits):
    print(f'{index}: {fruit}')
# 0: apple   1: banana   2: cherry
```

### 7.5 `break`, `continue`, `pass`

| Keyword | Effect |
|---|---|
| `break` | Immediately exits the loop |
| `continue` | Skips rest of current iteration |
| `pass` | Does nothing — placeholder for empty blocks |

```python
# break — stop at 5
for i in range(10):
    if i == 5:
        break
    print(i)    # 0 1 2 3 4

# continue — skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)    # 1 3 5 7 9
```

### 7.6 Nested Loops

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f'{i} x {j} = {i*j}')

# Star pattern
for i in range(1, 6):
    print('*' * i)
# *  **  ***  ****  *****
```

---

## Chapter 8 — Functions

### 8.1 Defining and Calling Functions

```python
def greet():
    print('Hello, there!')
    print('Welcome to Python!')

greet()   # Call the function
greet()   # Can call multiple times
```

### 8.2 Parameters and Arguments

```python
def greet(name):
    print(f'Hello, {name}!')

greet('Alice')   # Hello, Alice!
greet('Bob')     # Hello, Bob!

# Multiple parameters
def add(a, b):
    result = a + b
    print(f'{a} + {b} = {result}')

add(3, 5)        # 3 + 5 = 8
```

### 8.3 Return Values

```python
def square(n):
    return n ** 2

result = square(5)
print(result)       # 25

# Return multiple values (as a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 7, 2, 9])
print(f'Min: {low}, Max: {high}')   # Min: 1, Max: 9
```

### 8.4 Default & Keyword Arguments

```python
# Default argument — used if not provided
def power(base, exp=2):
    return base ** exp

print(power(3))      # 9   (exp defaults to 2)
print(power(3, 3))   # 27

# Keyword arguments — order doesn't matter
def describe(name, age, city):
    print(f'{name}, {age}, from {city}')

describe(age=25, city='Delhi', name='Alice')
```

### 8.5 `*args` and `**kwargs`

```python
# *args — accept any number of positional arguments
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3))          # 6
print(add_all(10, 20, 30, 40))   # 100

# **kwargs — accept any number of keyword arguments
def show_info(**details):
    for key, value in details.items():
        print(f'{key}: {value}')

show_info(name='Alice', age=25, city='Delhi')
```

### 8.6 Variable Scope (Local vs Global)

```python
x = 10   # Global variable

def my_func():
    y = 20   # Local — only exists inside function
    print(x)  # Can READ global: 10
    print(y)  # 20

my_func()
# print(y)  ← NameError! y doesn't exist here

# To MODIFY a global variable inside a function:
count = 0
def increment():
    global count
    count += 1

increment()
print(count)   # 1
```

---

## Chapter 9 — Lists

### 9.1 Creating Lists

```python
fruits  = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5]
mixed   = [42, 'hello', 3.14, True]
empty   = []
nested  = [[1, 2], [3, 4], [5, 6]]

print(fruits)        # ['apple', 'banana', 'cherry']
print(len(fruits))   # 3
```

### 9.2 Indexing & Slicing

```python
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

print(fruits[0])      # apple
print(fruits[-1])     # elderberry
print(fruits[1:3])    # ['banana', 'cherry']
print(fruits[:3])     # ['apple', 'banana', 'cherry']
print(fruits[2:])     # ['cherry', 'date', 'elderberry']
print(fruits[::2])    # every other element
print(fruits[::-1])   # reversed list
```

### 9.3 Modifying Lists

```python
fruits = ['apple', 'banana', 'cherry']

fruits[1] = 'blueberry'     # Change element
fruits.append('date')        # Add to end
fruits.insert(1, 'avocado')  # Insert at position
fruits.remove('cherry')      # Remove by value
removed = fruits.pop(0)      # Remove by index (returns it)
del fruits[0]                # Delete by index
```

### 9.4 List Methods Reference

| Method | Description |
|---|---|
| `.append(x)` | Add x to the end |
| `.insert(i, x)` | Insert x at position i |
| `.remove(x)` | Remove first occurrence of x |
| `.pop(i)` | Remove & return item at index i |
| `.sort()` | Sort list in-place (ascending) |
| `.sort(reverse=True)` | Sort descending |
| `.reverse()` | Reverse list in-place |
| `.index(x)` | Return index of first x |
| `.count(x)` | Count occurrences of x |
| `.extend(list2)` | Add all items from list2 |
| `.clear()` | Remove all items |
| `.copy()` | Return a shallow copy |

### 9.5 List Comprehensions

```python
# Syntax: [expression  for  item  in  iterable  if  condition]

# Squares of 1-10
squares = [x**2 for x in range(1, 11)]
print(squares)   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Even numbers only
evens = [x for x in range(20) if x % 2 == 0]

# Celsius to Fahrenheit
celsius    = [0, 20, 37, 100]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print(fahrenheit)   # [32.0, 68.0, 98.6, 212.0]

# Filter and transform
words = ['apple', 'Banana', 'cherry', 'Date']
upper = [w.upper() for w in words if len(w) > 5]
```

---

## Chapter 10 — Tuples, Sets & Dictionaries

### 10.1 Tuples

An **ordered, immutable** collection. Use for data that should never change.

```python
point  = (3, 7)
colors = ('red', 'green', 'blue')
single = (42,)   # ⚠️ Note the trailing comma!

print(colors[0])    # red
print(colors[-1])   # blue

# Tuple unpacking
x, y = point
print(f'x={x}, y={y}')   # x=3, y=7
```

### 10.2 Sets

An **unordered collection of unique elements**. Great for removing duplicates and set operations.

```python
fruits = {'apple', 'banana', 'cherry'}
empty  = set()   # NOT {} — that creates a dict!

# Automatically removes duplicates
dupes = {1, 2, 2, 3, 3, 3}
print(dupes)   # {1, 2, 3}

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)    # Union:         {1,2,3,4,5,6}
print(a & b)    # Intersection:  {3,4}
print(a - b)    # Difference:    {1,2}
print(a ^ b)    # Symmetric diff:{1,2,5,6}

# Remove duplicates from a list
data   = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(data))
```

### 10.3 Dictionaries

Stores **key-value pairs**. Keys must be unique and immutable.

```python
person = {
    'name':       'Alice',
    'age':        25,
    'city':       'Delhi',
    'is_student': True
}

# Accessing values
print(person['name'])             # Alice
print(person.get('age'))          # 25
print(person.get('job', 'N/A'))   # N/A  (safe default)

# Modifying
person['age']   = 26                     # Update
person['email'] = 'alice@example.com'    # Add new key
del person['city']                        # Delete

# Iterating
for key, value in person.items():
    print(f'{key}: {value}')
```

### 10.4 Dictionary Methods

| Method | Description |
|---|---|
| `.keys()` | Returns all keys |
| `.values()` | Returns all values |
| `.items()` | Returns all (key, value) pairs |
| `.get(key, default)` | Safe access with fallback |
| `.update(dict2)` | Merge another dictionary |
| `.pop(key)` | Remove key, return its value |
| `.clear()` | Remove all items |
| `key in dict` | Check if key exists |

---

## Chapter 11 — Lambda, Map, Filter & Reduce

### 11.1 Lambda Functions

A **small anonymous function** defined in one line.

```python
# Syntax: lambda parameters : expression

# Regular function vs lambda
def square(x):
    return x ** 2

square_l = lambda x: x ** 2

print(square(5))     # 25
print(square_l(5))   # 25

# Multiple parameters
add      = lambda a, b: a + b
multiply = lambda a, b, c: a * b * c

print(add(3, 5))           # 8
print(multiply(2, 3, 4))   # 24
```

### 11.2 Sorting with Lambda

```python
students = [
    {'name': 'Alice', 'gpa': 3.8},
    {'name': 'Bob',   'gpa': 3.5},
    {'name': 'Carol', 'gpa': 3.9},
]

# Sort by GPA
students.sort(key=lambda s: s['gpa'])

# Sort strings by length
words = ['banana', 'apple', 'kiwi', 'cherry']
words.sort(key=lambda w: len(w))
print(words)   # ['kiwi', 'apple', 'banana', 'cherry']
```

### 11.3 `map()`

Applies a function to **every item** in an iterable.

```python
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, numbers))
print(squares)   # [1, 4, 9, 16, 25]

# Convert list of strings to uppercase
names = ['alice', 'bob', 'carol']
upper = list(map(str.upper, names))
print(upper)     # ['ALICE', 'BOB', 'CAROL']
```

### 11.4 `filter()`

Keeps only items where the function returns `True`.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6, 8, 10]

words = ['hi', 'hello', 'hey', 'howdy', 'greetings']
long  = list(filter(lambda w: len(w) > 4, words))
print(long)    # ['hello', 'howdy', 'greetings']
```

### 11.5 `reduce()`

```python
from functools import reduce

nums    = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, nums)
print(product)   # 120  (1*2*3*4*5)

maximum = reduce(lambda a, b: a if a > b else b, nums)
print(maximum)   # 5
```

---

## Chapter 12 — Object-Oriented Programming — Classes

### 12.1 What is OOP?

| OOP Concept | Real-World Analogy |
|---|---|
| Class | Blueprint of a house |
| Object / Instance | An actual house built from the blueprint |
| Attribute | Properties: color, size, rooms |
| Method | Actions: open door, turn on lights |
| Constructor (`__init__`) | The moment the house is built |

### 12.2 Creating a Class

```python
class Dog:
    # Class variable — shared by ALL instances
    species = 'Canis lupus familiaris'

    # Constructor — called when object is created
    def __init__(self, name, age, breed):
        self.name  = name    # Instance variable
        self.age   = age
        self.breed = breed

    def bark(self):
        print(f'{self.name} says: Woof!')

    def describe(self):
        print(f'{self.name} is a {self.age}-year-old {self.breed}')

# Create objects (instances)
dog1 = Dog('Rex', 3, 'German Shepherd')
dog2 = Dog('Bella', 5, 'Labrador')

dog1.bark()      # Rex says: Woof!
dog2.describe()  # Bella is a 5-year-old Labrador
print(Dog.species)
```

### 12.3 The `__str__` Method

```python
class Car:
    def __init__(self, make, model, year):
        self.make  = make
        self.model = model
        self.year  = year

    def __str__(self):
        return f'{self.year} {self.make} {self.model}'

car = Car('Toyota', 'Camry', 2023)
print(car)       # 2023 Toyota Camry
```

### 12.4 Static and Class Methods

```python
class MathHelper:
    pi = 3.14159

    @staticmethod           # No self or cls
    def add(a, b):
        return a + b

    @classmethod            # Receives the class as cls
    def circle_area(cls, r):
        return cls.pi * r ** 2

print(MathHelper.add(3, 5))          # 8
print(MathHelper.circle_area(7))     # 153.93...
```

---

## Chapter 13 — Inheritance & Polymorphism

### 13.1 Inheritance

```python
# Parent (Base) class
class Animal:
    def __init__(self, name):
        self.name  = name
        self.alive = True

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')

# Child classes inherit from Animal
class Dog(Animal):
    def bark(self):
        print(f'{self.name} says: Woof!')

class Cat(Animal):
    def meow(self):
        print(f'{self.name} says: Meow!')

dog = Dog('Rex')
dog.eat()    # Rex is eating   ← inherited
dog.bark()   # Rex says: Woof! ← own method
```

### 13.2 `super()` and Method Overriding

```python
class Vehicle:
    def __init__(self, make, model):
        self.make  = make
        self.model = model

    def describe(self):
        print(f'{self.make} {self.model}')

class ElectricCar(Vehicle):
    def __init__(self, make, model, battery_kwh):
        super().__init__(make, model)   # Call parent __init__
        self.battery_kwh = battery_kwh

    def describe(self):                 # Override parent method
        super().describe()              # Call parent version
        print(f'Battery: {self.battery_kwh} kWh')

tesla = ElectricCar('Tesla', 'Model 3', 75)
tesla.describe()
# Tesla Model 3
# Battery: 75 kWh
```

### 13.3 Polymorphism

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h

# Same interface — different behavior
shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
for shape in shapes:
    print(f'Area: {shape.area():.2f}')
```

### 13.4 Duck Typing

> *"If it walks like a duck and quacks like a duck, it IS a duck."*

```python
class Duck:
    def sound(self): print('Quack!')

class Person:
    def sound(self): print("I'm quacking like a duck!")

class Robot:
    def sound(self): print('BLEEP BLOOP — QUACK')

# All work the same way — Python doesn't care about type!
things = [Duck(), Person(), Robot()]
for thing in things:
    thing.sound()
```

---

## Chapter 14 — Magic Methods & Properties

### 14.1 Magic (Dunder) Methods

| Method | Triggered By |
|---|---|
| `__init__(self, ...)` | Object creation: `MyClass()` |
| `__str__(self)` | `str(obj)`, `print(obj)` |
| `__repr__(self)` | `repr(obj)` |
| `__len__(self)` | `len(obj)` |
| `__add__(self, other)` | `obj1 + obj2` |
| `__sub__(self, other)` | `obj1 - obj2` |
| `__mul__(self, other)` | `obj1 * obj2` |
| `__eq__(self, other)` | `obj1 == obj2` |
| `__lt__(self, other)` | `obj1 < obj2` |
| `__contains__(self, item)` | `'x' in obj` |
| `__getitem__(self, key)` | `obj[key]` |

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

v1 = Vector(2, 3)
v2 = Vector(4, 1)
print(v1 + v2)     # Vector(6, 4)
print(v1 * 3)      # Vector(6, 9)
print(v1 == v2)    # False
```

### 14.2 Property Decorators

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError('Temperature below absolute zero!')
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

t = Temperature(100)
print(t.celsius)     # 100
print(t.fahrenheit)  # 212.0
t.celsius = 25       # Uses the setter
# t.celsius = -300   ← raises ValueError
```

---

## Chapter 15 — Exception Handling

### 15.1 Common Exceptions

| Exception | Cause |
|---|---|
| `ValueError` | Wrong value type: `int('abc')` |
| `ZeroDivisionError` | Division by zero: `1 / 0` |
| `TypeError` | Wrong type: `'2' + 2` |
| `IndexError` | List index out of range |
| `KeyError` | Dictionary key not found |
| `FileNotFoundError` | File doesn't exist |
| `AttributeError` | Object has no such attribute |
| `NameError` | Variable not defined |

### 15.2 try / except / else / finally

```python
try:
    num    = int(input('Enter a number: '))
    result = 100 / num
except ValueError:
    print('That is not a valid number!')
except ZeroDivisionError:
    print('Cannot divide by zero!')
except Exception as e:
    print(f'Unexpected error: {e}')
else:
    # Runs ONLY if no exception occurred
    print(f'Result: {result}')
finally:
    # ALWAYS runs — use for cleanup
    print('Thank you for using the calculator!')
```

### 15.3 Raising Exceptions

```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError('Age must be an integer')
    if age < 0 or age > 150:
        raise ValueError(f'Age {age} is out of range (0-150)')
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f'Error: {e}')
```

### 15.4 Custom Exceptions

```python
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount  = amount
        self.balance = balance
        super().__init__(f'Cannot withdraw ${amount}. Balance: ${balance}')

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(amount, self.balance)
        self.balance -= amount
        return self.balance

account = BankAccount(100)
try:
    account.withdraw(200)
except InsufficientFundsError as e:
    print(e)
```

---

## Chapter 16 — File Handling

### 16.1 File Modes

| Mode | Description |
|---|---|
| `'r'` | Read (default) — file must exist |
| `'w'` | Write — creates file, overwrites if exists |
| `'a'` | Append — adds to end of file |
| `'x'` | Create — fails if file already exists |
| `'r+'` | Read and write |
| `'b'` | Binary mode (add to above: `'rb'`, `'wb'`) |

### 16.2 Reading Files

```python
# Read entire file — recommended way (auto-closes)
with open('greetings.txt', 'r') as file:
    content = file.read()
    print(content)

# Read line by line
with open('greetings.txt', 'r') as file:
    for line in file:
        print(line.strip())   # strip() removes \n

# Read all lines into a list
with open('greetings.txt', 'r') as file:
    lines = file.readlines()
```

### 16.3 Writing Files

```python
# Write to a text file
with open('output.txt', 'w') as file:
    file.write('Hello, File!\n')
    file.write('Second line\n')

# Append to existing file
with open('output.txt', 'a') as file:
    file.write('Third line\n')
```

### 16.4 Working with JSON

```python
import json

# Python dict → JSON file
person = {'name': 'Alice', 'age': 25, 'skills': ['Python', 'SQL']}

with open('person.json', 'w') as f:
    json.dump(person, f, indent=4)

# JSON file → Python dict
with open('person.json', 'r') as f:
    data = json.load(f)
    print(data['name'])     # Alice
    print(data['skills'])   # ['Python', 'SQL']
```

### 16.5 Working with CSV

```python
import csv

# Writing CSV
with open('students.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'GPA'])
    writer.writerow(['Alice', 25, 3.8])
    writer.writerow(['Bob',   22, 3.5])

# Reading CSV
with open('students.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### 16.6 `os` Module for File Operations

```python
import os

print(os.path.exists('output.txt'))    # True or False
print(os.path.isfile('output.txt'))    # True
print(os.path.isdir('my_folder'))      # True
print(os.path.getsize('output.txt'))   # bytes
print(os.listdir('.'))                 # files in current dir

os.makedirs('new_folder', exist_ok=True)
os.rename('old.txt', 'new.txt')
os.remove('unwanted.txt')
```

---

## Chapter 17 — Modules, Packages & Standard Library

### 17.1 Importing Modules

```python
# Import full module
import math
print(math.sqrt(16))   # 4.0

# Import specific items
from math import sqrt, pi, ceil
print(sqrt(25))        # 5.0

# Import with alias
import random as rnd
print(rnd.randint(1, 10))

# Import everything (not recommended)
from math import *
```

### 17.2 Creating Your Own Module

```python
# === File: mymath.py ===
PI = 3.14159

def circle_area(r):
    return PI * r ** 2

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True


# === File: main.py ===
import mymath

print(mymath.circle_area(5))
print(mymath.is_prime(17))   # True
```

### 17.3 Key Standard Library Modules

| Module | Purpose |
|---|---|
| `math` | Math functions: `sqrt()`, `pi`, `ceil()` |
| `random` | Random numbers: `randint()`, `choice()` |
| `os` | OS operations: `listdir()`, `path` |
| `sys` | System info: `argv`, `exit()` |
| `datetime` | Dates & times: `datetime.now()` |
| `json` | JSON read/write: `load()`, `dump()` |
| `csv` | CSV read/write: `reader()`, `writer()` |
| `re` | Regular expressions: `search()`, `match()` |
| `collections` | Counter, defaultdict, deque |
| `time` | Time functions: `sleep()` |
| `pathlib` | Modern file paths: `Path()` |
| `hashlib` | Cryptographic hashes: `sha256()` |

### 17.4 `datetime` Module

```python
from datetime import datetime, date, timedelta

now   = datetime.now()
today = date.today()

print(now)                            # 2024-01-15 10:30:45
print(now.strftime('%B %d, %Y'))      # January 15, 2024

# Date arithmetic
birthday  = date(2000, 5, 15)
age_days  = (today - birthday).days
next_week = today + timedelta(days=7)
print(f'Age in days: {age_days}')
```

---

## Chapter 18 — Decorators & Generators

### 18.1 Decorators

A decorator **wraps another function** to add functionality without modifying it.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('--- Before function ---')
        result = func(*args, **kwargs)
        print('--- After function  ---')
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f'Hello, {name}!')

greet('Alice')
# --- Before function ---
# Hello, Alice!
# --- After function  ---
```

### 18.2 Practical Decorator Examples

```python
import time

# Timing decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start  = time.time()
        result = func(*args, **kwargs)
        end    = time.time()
        print(f'{func.__name__} ran in {end-start:.4f}s')
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return 'Done'

slow_function()   # slow_function ran in 1.0012s
```

### 18.3 Generators

A generator uses `yield` to produce values **lazily** — one at a time — saving memory.

```python
# Regular function — returns all at once
def squares_list(n):
    return [x**2 for x in range(n)]

# Generator — produces one at a time
def squares_gen(n):
    for x in range(n):
        yield x ** 2

for sq in squares_gen(5):
    print(sq)   # 0 1 4 9 16

# Infinite generator — impossible with a list!
def count_up(start=0):
    while True:
        yield start
        start += 1

counter = count_up(1)
print(next(counter))   # 1
print(next(counter))   # 2
print(next(counter))   # 3
```

### 18.4 Generator Expressions

```python
# Like list comprehension but lazy — uses () instead of []
squares = (x**2 for x in range(10))
print(type(squares))   # <class 'generator'>

# Very memory efficient for large data
total = sum(x**2 for x in range(1_000_000))
print(total)
```

---

## Chapter 19 — Multithreading & APIs

### 19.1 Why Multithreading?

Multithreading runs **multiple tasks concurrently** — great for IO-bound tasks (network requests, file operations, UI).

```python
import threading
import time

def task(name, duration):
    print(f'Task {name} started')
    time.sleep(duration)
    print(f'Task {name} finished after {duration}s')

# Create threads
t1 = threading.Thread(target=task, args=('A', 2))
t2 = threading.Thread(target=task, args=('B', 1))
t3 = threading.Thread(target=task, args=('C', 3))

# Start all threads
t1.start(); t2.start(); t3.start()

# Wait for all to complete
t1.join(); t2.join(); t3.join()

print('All tasks complete!')
# Total time: ~3s instead of 6s!
```

### 19.2 Thread Safety — Locks

```python
import threading

counter = 0
lock    = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:    # Only one thread at a time
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()
print(counter)   # 500000  (correct — no race condition)
```

### 19.3 Working with Web APIs

```python
# pip install requests
import requests

url      = 'https://api.coindesk.com/v1/bpi/currentprice.json'
response = requests.get(url)

print(response.status_code)   # 200 = success

data      = response.json()
btc_price = data['bpi']['USD']['rate']
print(f'Bitcoin price: ${btc_price}')
```

### 19.4 Weather App — Full Example

```python
import requests

API_KEY = 'your_openweather_api_key'

def get_weather(city):
    url    = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()   # Raises on 4xx/5xx
        data = response.json()

        name     = data['name']
        temp     = data['main']['temp']
        feels    = data['main']['feels_like']
        desc     = data['weather'][0]['description']
        humidity = data['main']['humidity']

        print(f'\n=== Weather in {name} ===')
        print(f'Temperature: {temp}°C (feels like {feels}°C)')
        print(f'Condition:   {desc.capitalize()}')
        print(f'Humidity:    {humidity}%')

    except requests.exceptions.HTTPError as e:
        print(f'HTTP Error: {e}')
    except requests.exceptions.ConnectionError:
        print('No internet connection!')

city = input('Enter city: ')
get_weather(city)
```

---

## Chapter 20 — GUI Development & Final Projects

### 20.1 Introduction to PyQt5

```bash
pip install PyQt5
```

```python
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My First GUI App')
        self.setGeometry(100, 100, 600, 400)

        label = QLabel('Hello, PyQt5!', self)
        label.setFont(QFont('Arial', 24))
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
```

### 20.2 Common PyQt5 Widgets

| Widget Class | Purpose |
|---|---|
| `QLabel` | Display text or images |
| `QPushButton` | Clickable button |
| `QLineEdit` | Single-line text input |
| `QTextEdit` | Multi-line text area |
| `QCheckBox` | Toggle on/off checkbox |
| `QRadioButton` | Single-choice option |
| `QComboBox` | Dropdown selection |
| `QSlider` | Slider control |
| `QProgressBar` | Progress indicator |
| `QMessageBox` | Popup dialog box |
| `QFileDialog` | Open/save file dialog |
| `QTimer` | Repeating or one-shot timer |

### 20.3 Layouts

```python
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel,
    QVBoxLayout, QHBoxLayout, QGridLayout)

# Vertical layout — stacks top to bottom
vbox = QVBoxLayout()
vbox.addWidget(QLabel('Name:'))
vbox.addWidget(QLabel('Age:'))

# Horizontal layout — side by side
hbox = QHBoxLayout()
hbox.addWidget(QPushButton('OK'))
hbox.addWidget(QPushButton('Cancel'))

# Grid layout — like a table
grid = QGridLayout()
grid.addWidget(QPushButton('7'), 0, 0)
grid.addWidget(QPushButton('8'), 0, 1)
grid.addWidget(QPushButton('9'), 0, 2)
```

### 20.4 Signals and Slots

```python
class Counter(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0

        self.label = QLabel('Count: 0', self)
        self.label.setFont(QFont('Arial', 20))

        btn_inc = QPushButton('+ Increment')
        btn_dec = QPushButton('- Decrement')
        btn_rst = QPushButton('Reset')

        # Connect signals to slots
        btn_inc.clicked.connect(self.increment)
        btn_dec.clicked.connect(self.decrement)
        btn_rst.clicked.connect(self.reset)

    def increment(self):
        self.count += 1
        self.label.setText(f'Count: {self.count}')

    def decrement(self):
        self.count -= 1
        self.label.setText(f'Count: {self.count}')

    def reset(self):
        self.count = 0
        self.label.setText('Count: 0')
```

### 20.5 Final Projects Summary

| Project | Key Concepts Used |
|---|---|
| Hello World & Variables | Ch 1–3: print, input, variables, casting |
| Calculator | Ch 5–6: math operators, if-elif-else |
| Number Guessing Game | Ch 7–8: loops, random, functions |
| Hangman | Ch 9–10: lists, strings, ASCII art, files |
| Slot Machine | Ch 8–10: functions, random, collections |
| Encryption (Caesar Cipher) | Ch 4–8: string manipulation, loops |
| Banking System (OOP) | Ch 12–15: classes, inheritance, exceptions |
| Contact Book (File I/O) | Ch 16–17: JSON files, dictionaries, os module |
| Weather App (API) | Ch 19: requests, JSON, error handling |
| GUI Calculator (PyQt5) | Ch 20: widgets, layouts, signals/slots |
| Digital Clock (PyQt5) | Ch 20: QTimer, QTime, formatting |
| To-Do App (PyQt5 + JSON) | All chapters: full CRUD app with persistence |

---

## 🎓 Congratulations!

You have completed all **20 chapters** of Python programming — from `print("Hello World")` to full GUI desktop applications!

> 🐍 **Happy Coding, Bro!**
>
> Keep building, keep practicing. The best way to learn programming is by **writing code every single day**.
>
> 📖 **Resources:** [python.org](https://python.org) | [docs.python.org](https://docs.python.org) | [realpython.com](https://realpython.com)

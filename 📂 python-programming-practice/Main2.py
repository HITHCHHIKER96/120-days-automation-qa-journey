# arithmetic operations and build-in functions

x = 3.78
y = 5
z = 4

print(round(x)) # round of function
print(abs(y)) # abs() function is absolute value from the mentioned number to distance number
print(pow(y,z))
print(max(x,y,z))
print(min(x,y,z))

# VERY USEFUL CONSTRAINTS and MATH CLASS:

import math

print(math.pi)
print(math.sqrt(34))
print(math.ceil(4.6)) # ceil is a round of floating number
print(math.e)
print(math.floor(3.8)) # floor round down the floating number like 5.9 -> 5

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius
print(f"The circumference of the circle is: {circumference}")

area = round(math.pi * pow(radius, 2), 2)
print(f"The area of this circle is: {area}cm²") #shortcut key to put ^2 alt+0+1+7+8



# IF || ELSE :: DO SOME CODE IF SOME CONDITIONS ARE TRUE
#                 ELSE DO SOMETHING ELSE

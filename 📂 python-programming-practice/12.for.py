# for loops: execute a block of code a fixed number of times.
#            You can iterate over a range, string, sequence, etc.

for i in range(1,19,4): # if you want to count it by 2 spaced just add one more after that like - for x in range(1,23,3)
    print(i)
print("Happy Day")

# To reverse this loop just use REVERSED() methods
for x in reversed(range(1, 9)):
    print(x)
print("Happy Day")

# to iterate a string over for loop:
aadhar_number = "4733-3738-0872"
for x in aadhar_number:
    print(x)

# Suppose you want to skip an iteration over the loop use CONTINUE keyword
for x in range(1, 20):
    if x == 10:
        continue # It will skip number 10
    else:
        print(x)

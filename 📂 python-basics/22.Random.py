import random

# print(help(random))
num1 = 1
num2 = 1000
options = ("rock", "paper", "scissors")
cards = ["2","3","4","5","6","7","8","9","10","K","Q","J","A"]
# print(random.randint(num1, num2)) # to print random integer
# print(random.random()) # to print random floating point number
print(random.shuffle(cards)) # it will shuffle cards

print(random.choice(options)) # this choice() method is best for games

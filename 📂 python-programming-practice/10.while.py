# while loop = execute some code WHILE some condition remains true and it is better when you know the condition will be infinte number of times

food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit): ")
print("Bye")
# Using logical operator in while loop:

num = int(input("Enter the number between 1 to 100: "))
while not num > 1 or num < 100:
    print("It is not valid")
    num = int(input("Enter the number between 1 to 100: "))
print(f"Your number is {num}")

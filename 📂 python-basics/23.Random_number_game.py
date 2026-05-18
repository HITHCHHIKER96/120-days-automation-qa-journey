import random

lowest_number = 1
highest_number = 100
guessed_num= random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print("Python number testing game")
print(f"Enter a number between {lowest_number} and {highest_number}: ")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_number or guesses > highest_number:
            print("That number is out of range.")
            print(f"Enter a number between {lowest_number} and {highest_number}: ")
        elif guess < guessed_num:
            print("Too low!")
        elif guess > guessed_num:
            print("Too high!")
        else:
            print(f"That's CORRECT! The answer was: {guessed_num}")
            print(f"The number of guesses: {guess}")
            is_running = False
    else:
        print("Invalid guess.")
        print(f"Enter a number between {lowest_number} and {highest_number}: ")

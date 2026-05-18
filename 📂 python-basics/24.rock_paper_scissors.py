import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player_score = None
    computer = random.choice(options)

    while player_score not in options:
        player_score = input("Enter a choice (rock, paper, scissors): ")
    print(f"Player: {player_score}")
    print(f"Computer: {computer}")

    if player_score == computer:
        print("It's a tie!")
    elif player_score == "rock" and computer == "scissors":
        print(f"Winner is: {player_score}!")
    elif player_score == "scissors" and computer == "paper":
        print(f"Winner is: {player_score}!")
    elif player_score == "paper" and computer == "rock":
        print(f"Winner is: {player_score}!")
    else:
        print("You lose!")

    wanna_play = input("Want to play again? (Y/N): ")
    if not wanna_play == "Y":
        running = False
print("See You!")

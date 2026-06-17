# Python Slot Machine
import random


def spin_row():
    symbols = ['🍒','🍉','🥭','🔔']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*********")
    print(" || ".join(row))
    print("*********")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 30
        elif row[0] == '🍉':
            return bet * 49
        elif row[0] == '🥭':
            return bet * 67
        elif row[0] == '🔔':
            return bet * 100
    return 0

def main():
    balance = 10000

    print("********************")
    print(" Welcome to Slot machine game ")
    print("Symbols: 🍒 🍉 🥭 🔔 ")
    print("******************")

    while balance > 0:
        print(f"Current Balance:{balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than zero.")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning.....\n")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won {payout}")
        else:
            print("Sorry! You lost this round")
        balance += payout

        play_again = input("You want to play again? (Y/N): ").upper()

        if play_again != "Y":
            break

if __name__ == '__main__':
    main()

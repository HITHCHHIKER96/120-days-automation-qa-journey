# Python Slot Machine

def spin_row():
    pass

def print_row():
    pass

def get_payout():
    pass

def main():
    balance = 100

    print("********************")
    print(" Welcome to Slot machine game ")
    print("Symbols: 🍒 🍉 🥭 🔔 ")
    print("******************")

    while balance > 0:
        print(f"Current Balance:{balance}")
        bet = input("Place your bet amount: ")

        if  not bet.isdigit():
            print("Please enter a valid number.")
            continue

if __name__ == '__main__':
    main()

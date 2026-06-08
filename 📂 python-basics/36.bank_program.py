# Python Bank Program:

def show_balance():
    print(f"Your current balance is: ${balance:.2f}")

def deposit():
    money = float(input("Enter the money you want to deposit: "))
    if money < 0:
        print("Put a valid amount of money")
        return 0
    else:
        return money

def withdraw():
    w_money = float(input("Enter the money you want to withdraw: "))
    if w_money > balance:
        print("Insufficient Balance.")
        return 0
    elif w_money < 0:
        print("Enter the valid amount money want to withdraw.")
        return 0
    else:
        return w_money

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Python Bank Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("5. Exit.")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_balance()
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw()
        elif choice == '4':
            is_running = False
        else:
            print("This is not a valid choice")

    print("Thank you! Have a nice day.")

if __name__ == '__main__':
    main()

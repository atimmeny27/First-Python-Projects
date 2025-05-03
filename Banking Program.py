def show_balance(balance):  # Takes balance as a parameter
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("How much would you like to deposit?: "))
    if amount < 0:
        print("Not a valid amount")
        return 0  # Returns 0 if the deposit is invalid
    else:
        return amount  # Returns the valid deposit amount

def withdraw(balance):  # Takes balance as a parameter
    amount = float(input("How much would you like to withdraw?: "))
    if amount < 0:
        print("Not a valid amount")
        return 0  # Returns 0 if the withdrawal is invalid
    elif amount > balance:  # Checks if there are enough funds before returning the amount
        print("You don't have that much money")
        return 0  # Returns 0 if there are not enough funds
    else:
        return amount  # Returns valid withdrawal amount

balance = 0
is_running = True

while is_running:
    print("\n Banking Program")
    print("------------------")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")  # Correct string comparison

    if choice == "1":
        show_balance(balance)  # Corrected missing argument
    elif choice == "2":
        balance += deposit()  # Adds deposit amount to balance
    elif choice == "3":
        balance -= withdraw(balance)  # Passes balance to withdraw function
    elif choice == "4":
        is_running = False  # Exits the loop
    else:
        print("Not a valid choice")

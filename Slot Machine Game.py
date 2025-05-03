import random


def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔"]
    return [random.choice(symbols) for _ in range(3)]  # List comprehension for cleaner code


def print_row(row):
    print(" | ".join(row))


def get_payout(row, bet):
    multipliers = {'🍒': 25, '🍉': 7, '🍋': 7, '🔔': 50}

    if row[0] == row[1] == row[2]:  # All three symbols match
        return bet * multipliers[row[0]]  # Lookup the payout multiplier
    return 0


def main():
    balance = 10000
    print("---------------------------")
    print("Welcome to slots in Python")
    print("Symbols: 🍒 🍉 🍋 🔔")
    print("---------------------------")

    while balance > 0:
        print(f"Current Balance: ${balance}")
        bet = input("Place bet amount: ")

        if not bet.isdigit() or int(bet) <= 0:
            print("Not a valid bet amount")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient Funds")
            continue

        balance -= bet  # Deducts bet from balance

        print("\nSpinning...")
        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("You lost")

        balance += payout  # Add winnings to balance

        print(f"New Balance: ${balance}\n")  # Display updated balance

    print("Game Over! You're out of money.")


main()

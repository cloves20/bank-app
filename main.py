
import json
import os

DATA_FILE = "bank_data.json"


# Load saved account data
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)

            return data["balance"], data["transactions"]

        except (json.JSONDecodeError, KeyError, TypeError):
            print("Warning: Saved data could not be loaded.")

    return 1600, []


# Save account data
def save_data(balance, transactions):
    data = {
        "balance": balance,
        "transactions": transactions
    }

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# Deposit money
def deposit(balance, amount, transactions):
    if amount <= 0:
        print("Deposit must be greater than zero.")
        return balance

    balance += amount
    transactions.append(f"Deposit: +{amount}")

    print("Deposit successful!")
    return balance


# Withdraw money
def withdraw(balance, amount, transactions):
    if amount <= 0:
        print("Withdrawal must be greater than zero.")
        return balance

    if amount > balance:
        print("Insufficient funds.")
        return balance

    balance -= amount
    transactions.append(f"Withdrawal: -{amount}")

    print("Withdrawal successful!")
    return balance


# Get a valid whole number
def get_amount(prompt):
    try:
        return int(input(prompt))

    except ValueError:
        print("Please enter a valid whole number.")
        return None


# Display transaction history
def show_transactions(transactions):
    print("\n--- Transaction History ---")

    if not transactions:
        print("No transactions yet.")
    else:
        for transaction in transactions:
            print(transaction)

    print("---------------------------")


# Main application
def main():
    balance, transactions = load_data()
    choice = 0

    while choice != 5:
        print("\n===== Welcome to the Bank! =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Transaction history")
        print("5. Exit")

        try:
            choice = int(input("Choose an option: "))

        except ValueError:
            print("Please enter a valid menu number.")
            continue

        if choice == 1:
            amount = get_amount("Enter deposit amount: ")

            if amount is not None:
                old_balance = balance
                balance = deposit(balance, amount, transactions)

                if balance != old_balance:
                    save_data(balance, transactions)

                print("Current balance:", balance)

        elif choice == 2:
            amount = get_amount("Enter withdrawal amount: ")

            if amount is not None:
                old_balance = balance
                balance = withdraw(balance, amount, transactions)

                if balance != old_balance:
                    save_data(balance, transactions)

                print("Current balance:", balance)

        elif choice == 3:
            print("Current balance:", balance)

        elif choice == 4:
            show_transactions(transactions)

        elif choice == 5:
            print("Goodbye!")

        else:
            print("Invalid choice. Please select 1–5.")


if __name__ == "__main__":
    main()


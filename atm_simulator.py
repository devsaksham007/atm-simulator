"""A simple PIN-based ATM simulator."""

CORRECT_PIN = "1234"
MAX_LOGIN_ATTEMPTS = 3


def check_balance(balance):
    """Display the current account balance."""
    print(f"\nCurrent balance: ${balance:.2f}")
    return balance


def deposit(balance):
    """Deposit a positive amount and return the updated balance."""
    try:
        amount = float(input("Enter deposit amount: $"))
    except ValueError:
        print("Please enter a valid number.")
        return balance

    if amount <= 0:
        print("Deposit amount must be greater than zero.")
        return balance

    balance += amount
    print(f"Deposit successful. New balance: ${balance:.2f}")
    return balance


def withdraw(balance):
    """Withdraw an amount when it is positive and available."""
    try:
        amount = float(input("Enter withdrawal amount: $"))
    except ValueError:
        print("Please enter a valid number.")
        return balance

    if amount <= 0:
        print("Withdrawal amount must be greater than zero.")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print(f"Withdrawal successful. New balance: ${balance:.2f}")

    return balance


def login():
    """Return True after a successful PIN entry, otherwise return False."""
    for attempt in range(MAX_LOGIN_ATTEMPTS):
        pin = input("Enter your 4-digit PIN: ")
        if pin == CORRECT_PIN:
            print("Login successful.")
            return True

        attempts_left = MAX_LOGIN_ATTEMPTS - attempt - 1
        if attempts_left:
            print(f"Incorrect PIN. Attempts left: {attempts_left}")

    print("Too many incorrect attempts. Account locked.")
    return False


def run_atm():
    """Run the ATM menu until the user chooses to exit."""
    if not login():
        return

    balance = 1000.00

    while True:
        print("\n--- ATM Menu ---")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    run_atm()

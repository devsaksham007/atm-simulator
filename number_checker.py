"""Interactive even, odd, and prime number checker."""


def is_even(number):
    """Return True when number is divisible by 2."""
    return number % 2 == 0


def is_prime(number):
    """Return True when number is a prime number."""
    if number < 2:
        return False

    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def describe_number(number):
    """Return a readable description of a number."""
    parity = "even" if is_even(number) else "odd"
    prime_status = "prime" if is_prime(number) else "not prime"
    return f"{number} is {parity} and {prime_status}."


def check_number():
    """Read one integer and print its properties."""
    value = input("Enter an integer: ").strip()

    try:
        number = int(value)
    except ValueError:
        print("Please enter a whole number.")
        return

    print(describe_number(number))


def check_number_list():
    """Read a space-separated list of integers and print each result."""
    values = input("Enter integers separated by spaces: ").split()
    numbers = []

    for value in values:
        try:
            numbers.append(int(value))
        except ValueError:
            print(f"Skipping '{value}': not a whole number.")

    if not numbers:
        print("No valid numbers were entered.")
        return

    print("\nResults:")
    for number in numbers:
        print(f"- {describe_number(number)}")


def run_checker():
    """Run the checker menu until the user chooses to exit."""
    while True:
        print("\n--- Even/Odd & Prime Number Checker ---")
        print("1. Check one number")
        print("2. Check a list of numbers")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            check_number()
        elif choice == "2":
            check_number_list()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    run_checker()

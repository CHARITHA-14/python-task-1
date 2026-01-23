def add(a, b=0):
    """Return sum of two numbers."""
    return a + b


def subtract(a, b=0):
    """Return difference of two numbers."""
    return a - b


def multiply(a, b=1):
    """Return product of two numbers."""
    return a * b


def divide(a, b=1):
    """Return division result."""
    if b == 0:
        raise ValueError("Division by zero not allowed")
    return a / b


def get_numbers():
    """Read two numbers from user."""
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b


def show_menu():
    """Display menu."""
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def main():
    """Run calculator."""
    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "5":
            print("Exiting...")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice")
            continue

        a, b = get_numbers()

        try:
            if choice == "1":
                print("Result:", add(a, b))
            elif choice == "2":
                print("Result:", subtract(a, b))
            elif choice == "3":
                print("Result:", multiply(a, b))
            elif choice == "4":
                print("Result:", divide(a, b))
        except ValueError as e:
            print("Error:", e)


def test_functions():
    """Test all functions."""
    print(add(2, 3))
    print(subtract(5, 2))
    print(multiply(4, 3))
    print(divide(8, 2))

    try:
        divide(5, 0)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    test_functions()
    main()
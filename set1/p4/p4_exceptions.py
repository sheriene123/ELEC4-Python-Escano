# Full Name: Sheriene Escano
# Section: IV-BSIT C
# Activity Code: P4
# Date: November 24, 2026


def divide_numbers():
    try:
        numerator = float(input("Enter the first number: "))
        denominator = float(input("Enter the second number: "))
        result = numerator / denominator
    except ValueError:
        print("Invalid number. Please enter a numeric value.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"Result: {result:g}")


def show_menu():
    print("\n===== Safe Menu Program =====")
    print("1. Divide two numbers")
    print("2. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            divide_numbers()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()

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


def open_file():
    filename = input("Enter the file name: ").strip()
    try:
        with open(filename, encoding="utf-8") as source:
            contents = source.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except UnicodeError:
        print("The file could not be read as UTF-8 text.")
    except (OSError, ValueError) as error:
        print(f"Could not open the file: {error}")
    else:
        print("\nFile contents:")
        print(contents)
    finally:
        # This message appears whether the file was read or an error occurred.
        print("File operation finished.")


def show_menu():
    print("\n===== Safe Menu Program =====")
    print("1. Divide two numbers")
    print("2. Open a text file")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            divide_numbers()
        elif choice == "2":
            open_file()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()

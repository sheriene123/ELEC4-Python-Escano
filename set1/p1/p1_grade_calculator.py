# Full Name: Sheriene Escano
# Section: IV-BSIT C
# Activity Code: P1
# Date: November 24, 2026


def enter_grades():
    """Accept grades and validate each value."""
    grades = []
    while True:
        value = input("Enter a grade (0-100), or type 'done': ").strip()
        if value.lower() == "done":
            if not grades:
                print("Enter at least one grade first.")
                continue
            return grades

        try:
            grade = float(value)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if 0 <= grade <= 100:
            grades.append(grade)
        else:
            print("Invalid grade. The grade must be from 0 to 100.")


def calculate_average(grades):
    """Return the average of a list of grades."""
    return sum(grades) / len(grades)


def get_highest_grade(grades):
    """Return the highest grade."""
    return max(grades)


def get_lowest_grade(grades):
    """Return the lowest grade."""
    return min(grades)


def get_pass_status(grades):
    """Determine pass/fail status using the passing average of 75."""
    average = calculate_average(grades)
    return "PASSED" if average >= 75 else "FAILED"


def display_results(grades):
    """Display all computed grade results."""
    if not grades:
        print("No grades entered yet.")
        return

    print("\nStudent Grade Results")
    print("Grades:", ", ".join(str(grade) for grade in grades))
    print(f"Average: {calculate_average(grades):.2f}")
    print(f"Highest Grade: {get_highest_grade(grades):.2f}")
    print(f"Lowest Grade: {get_lowest_grade(grades):.2f}")
    print(f"Status: {get_pass_status(grades)}")


def show_menu():
    print("\n===== Student Grade Calculator =====")
    print("1. Enter grades")
    print("2. View results")
    print("3. Exit")


def main():
    grades = []

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            grades = enter_grades()
        elif choice == "2":
            display_results(grades)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()


# A local variable is declared inside a function and exists only in that function.
# In this program, grades inside main is a local variable that holds the student's list.
# The grades parameter in functions such as calculate_average is also local to that function.
# A global variable is declared outside functions and can be used across the whole program.
# This program keeps most values local so the data stays controlled and easier to manage.

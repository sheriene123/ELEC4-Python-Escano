# Full Name: Sheriene Escano
# Section: IV-BSIT C
# Activity Code: P2
# Date: November 24, 2026

import student_utils
from student_utils import calculate_average
from datetime import datetime


def enter_grades():
    """Get validated grades from the user."""
    grades = []
    while True:
        entry = input("Enter a grade (0-100), or type 'done': ").strip()
        if entry.lower() == "done":
            if grades:
                return grades
            print("Please enter at least one grade.")
            continue

        try:
            grade = float(entry)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if 0 <= grade <= 100:
            grades.append(grade)
        else:
            print("The grade must be between 0 and 100.")


def main():
    grades = enter_grades()

    # Demonstrates importing a module with import module.
    highest = student_utils.get_highest_grade(grades)
    lowest = student_utils.get_lowest_grade(grades)
    status = student_utils.determine_status(grades)

    # Demonstrates importing a function with from module import name.
    average = calculate_average(grades)
    generated_at = datetime.now().strftime("%B %d, %Y at %I:%M:%S %p")

    print("\n===== Student Grade Report =====")
    print("Grades:", ", ".join(str(grade) for grade in grades))
    print(f"Average: {average:.2f}")
    print(f"Highest Grade: {highest:.2f}")
    print(f"Lowest Grade: {lowest:.2f}")
    print(f"Status: {status}")
    print(f"Report generated: {generated_at}")


if __name__ == "__main__":
    main()

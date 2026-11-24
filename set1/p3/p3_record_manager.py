# Full Name: Sheriene Escano
# Section: IV-BSIT C
# Activity Code: P3
# Date: November 24, 2026


def add_student(students, student_keys):
    name = input("Enter the student's name: ").strip()
    if not name:
        print("Please enter a name.")
        return

    key = name.casefold()
    if key in student_keys:
        print(f"{name} is already on the list.")
        return

    students.append(name)
    student_keys.add(key)
    print(f"Added {name}.")


def remove_student(students, student_keys):
    key = input("Enter the full name to remove: ").strip().casefold()
    if key not in student_keys:
        print("Student not found.")
        return

    # Remove the saved spelling and its matching key together.
    name = next(student for student in students if student.casefold() == key)
    students.remove(name)
    student_keys.remove(key)
    print(f"Removed {name}.")


def search_students(students):
    query = input("Enter all or part of a name: ").strip().casefold()
    if not query:
        print("Please enter a search term.")
        return

    matches = sorted(
        (name for name in students if query in name.casefold()),
        key=str.casefold,
    )
    if not matches:
        print("No matching students found.")
        return

    print("Search results:")
    for name in matches:
        print(f"- {name}")


def display_students(students):
    print("\nStudent list:")
    for number, name in enumerate(sorted(students, key=str.casefold), start=1):
        print(f"{number}. {name}")
    print(f"Total students: {len(students)}")


def show_menu():
    print("\n===== Student Record Manager =====")
    print("1. Add student")
    print("2. Remove student")
    print("3. Search students")
    print("4. Display all students")
    print("5. Exit")


def main():
    students = []
    student_keys = set()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students, student_keys)
        elif choice == "2":
            remove_student(students, student_keys)
        elif choice == "3":
            search_students(students)
        elif choice == "4":
            display_students(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()


# A list keeps items in order and can contain duplicates.
# The students list stores names as entered, which I sort when showing the list.
# A set keeps only unique values and supports fast membership checks.
# I use the student_keys set to detect duplicates regardless of capitalization.

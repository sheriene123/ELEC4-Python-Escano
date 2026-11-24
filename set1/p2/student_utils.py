# Full Name: Sheriene Escano
# Section: IV-BSIT C
# Activity Code: P2
# Date: November 24, 2026


def calculate_average(grades):
    """Calculate and return the average grade."""
    return sum(grades) / len(grades)


def determine_status(grades):
    """Return PASSED or FAILED based on an average of 75."""
    average = calculate_average(grades)
    return "PASSED" if average >= 75 else "FAILED"


def get_highest_grade(grades):
    """Return the highest grade."""
    return max(grades)


def get_lowest_grade(grades):
    """Return the lowest grade."""
    return min(grades)

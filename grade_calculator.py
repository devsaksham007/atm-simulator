"""Calculate a student's average mark and grade."""


def calculate_average(marks):
    """Return the average of a non-empty list of marks."""
    return sum(marks) / len(marks)


def assign_grade(average):
    """Return a letter grade for an average mark."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def read_marks():
    """Read and validate marks entered by the user."""
    while True:
        entry = input("Enter marks separated by spaces: ").strip()
        values = entry.split()
        marks = []

        if not values:
            print("Please enter at least one mark.")
            continue

        valid = True
        for value in values:
            try:
                mark = float(value)
            except ValueError:
                print(f"'{value}' is not a valid mark.")
                valid = False
                break

            if mark < 0 or mark > 100:
                print("Each mark must be between 0 and 100.")
                valid = False
                break

            marks.append(mark)

        if valid:
            return marks


def display_result(marks):
    """Print the marks, average, and assigned grade."""
    average = calculate_average(marks)
    grade = assign_grade(average)

    print("\n--- Grade Report ---")
    print("Marks:", ", ".join(f"{mark:g}" for mark in marks))
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")


def main():
    """Run the grade calculator."""
    print("Student Grade Calculator")
    marks = read_marks()
    display_result(marks)


if __name__ == "__main__":
    main()
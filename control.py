# Student Grading System
# Prevents marks above 100 or below 0

while True:

    student_name = input("\nEnter student name: ")
    number_of_subjects = int(input("Enter number of subjects: "))

    total_marks = 0
    total_points = 0

    # Lists to store subject details
    subjects = []
    marks_list = []
    grades = []
    points_list = []

    # Function to calculate grade and points
    def calculate_grade(mark):

        if mark >= 70:
            return "A", 12
        elif mark >= 60:
            return "B", 9
        elif mark >= 50:
            return "C", 6
        elif mark >= 40:
            return "D", 3
        else:
            return "F", 0

    # Enter subjects and marks
    for i in range(number_of_subjects):

        subject = input(f"\nEnter subject {i + 1} name: ")

        # Repeat until valid marks are entered
        while True:

            marks = float(input(f"Enter marks for {subject}: "))

            if marks > 100 or marks < 0:
                print("Invalid Marks! Please enter marks between 0 and 100.")
            else:
                break

        # Calculate grade and points
        grade, points = calculate_grade(marks)

        # Store values
        subjects.append(subject)
        marks_list.append(marks)
        grades.append(grade)
        points_list.append(points)

        total_marks += marks
        total_points += points

    # Calculate averages
    average_marks = total_marks / number_of_subjects
    average_points = total_points / number_of_subjects

    average_grade, avg_points = calculate_grade(average_marks)

    # Display Result Slip
    print("\n======================================================")
    print("                 STUDENT RESULT SLIP")
    print("======================================================")
    print(f"Student Name : {student_name}")
    print("======================================================")
    print(f"{'SUBJECT':<20}{'MARKS':<10}{'GRADE':<10}{'POINTS':<10}")
    print("======================================================")

    # Print all subjects
    for i in range(number_of_subjects):
        print(f"{subjects[i]:<20}{marks_list[i]:<10}{grades[i]:<10}{points_list[i]:<10}")

    print("======================================================")
    print(f"{'Total Marks':<20}: {total_marks}")
    print(f"{'Average Marks':<20}: {round(average_marks, 2)}")
    print(f"{'Average Grade':<20}: {average_grade}")
    print(f"{'Average Points':<20}: {round(average_points, 2)}")
    print("======================================================")

    # Continue or stop
    choice = input("\nDo you want to enter another student? (yes/no): ").lower()

    if choice != "yes":
        print("\nProgram Ended.")
        break
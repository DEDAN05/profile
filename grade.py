#!usr/bin/env python3
# creating the grading system
student_name = input("\n Enter your name: ")
print("\n {student_name}")
print("\n =========== Student Result===========")
while True:
    print("\n {student_name}")
    student_number_subject = int(input("\n Enter the number of subjects: "))
    print("\n {student_number_subject}")
    total_marks = 0
    total_points = 0

    # getting the lists of the subject and marks
    subject = []
    marks_lists = []
    grades = []
    points_lists = []

    #functions to calculate grades and marks
    def calculate_grades(marks):
        if marks > 100:
            print("\n Invalid Marks")
        elif marks >= 70:
            print("A", 12)
        elif marks >= 60 and <= 69:
            print("B", 10)


        

    

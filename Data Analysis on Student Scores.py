student_marks = {}

No_of_students = int(input("\nNo. of student's for which marks is to be entered: "))

i = 0
while i < No_of_students:
    name = input(f"\nEnter the name of student {i+1}: ")
    print("")
    while True:
        try:
            b = int(input(f"Enter the marks of {name}: "))
            if 0 <= b <= 100:
                student_marks[name] = b
                break
            else:
                print("Please enter valid Marks (0-100).")
        except ValueError:
            print("Invalid input. Please enter a number for the marks.")

    i += 1

marks_of_students = list(student_marks.values())
total_students = len(marks_of_students)

print("\nCollectively the marks of all the students are ", student_marks)
print("-" * 100)

if total_students == 0:
    print("No student data entered to calculate results.")
else:
   
    while True:
        print("\nNow what do you want to do")
        print("1. Calculate Class Average")
        print("2. Calculate The Highest/Lowest Marks")
        print("3. Calculate No. of Students Passed/Fail (Passing threshold is 40)")
        print("4. Passing Rate Percentage (Passing threshold is 40)")
        print("5. Display Individual Student Grades")
        print("6. Exit") 

        choice = 0
        while True:
            try:
                choice = int(input("\nEnter your choice(1,2,3,4,5,6): "))
                if 1 <= choice <= 6:
                    break
                else:
                    print("Please enter a choice between 1 and 6.")
            except ValueError:
                print("Invalid input. Please enter a number for your choice.")

        print("-" * 30)

        if choice == 6:
            print("Exiting the results analysis. Goodbye!")
            break # Exit the while True loop

        elif choice == 1:
            total_sum = sum(marks_of_students)
            Average = total_sum / total_students
            print("Your Class Average Is: {:.2f}".format(Average))

        elif choice == 2:
            Highest_Marks = max(marks_of_students)
            highest_scorers = [name for name, mark in student_marks.items() if mark == Highest_Marks]

            Lowest_Marks = min(marks_of_students)
            lowest_scorers = [name for name, mark in student_marks.items() if mark == Lowest_Marks]

            print(f"\nThe Highest Marks is {Highest_Marks} scored by: {', '.join(highest_scorers)}")
            print(f"The Lowest Marks is {Lowest_Marks} scored by: {', '.join(lowest_scorers)}")

        elif choice == 3:
            passing_threshold = 40
            pass_count = 0
            fail_count = 0

            for mark in marks_of_students:
                if mark >= passing_threshold:
                    pass_count += 1
                else:
                    fail_count += 1

            print(f"No Of Students Passed: **{pass_count}**")
            print(f"No Of Students Failed: **{fail_count}**")

        elif choice == 4:
            passing_threshold = 40
            students_passed = sum(1 for score in marks_of_students if score >= passing_threshold)

            passing_rate = (students_passed / total_students) * 100
            print(f"The total passing rate is: **{passing_rate:.2f}%**")

        elif choice == 5:
            def calculate_grade(marks):
                """
                Determines the student's grade based on the marks.
                """
                if marks >= 90:
                    return "Grade A+"
                elif marks >= 80:
                    return "Grade A"
                elif marks >= 70:
                    return "Grade B"
                elif marks >= 60:
                    return "Grade C"
                elif marks >= 40:
                    return "Grade D"
                else:
                    return "Grade F"

            print("--- Individual Student Grades ---")
            for name, marks in student_marks.items():
                grade = calculate_grade(marks)
                print(f"-->{name}--: {marks} -> __{grade}__")
        
        print("-" * 30) 
        print("-" * 30) 
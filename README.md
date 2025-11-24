 VITYARTHI-PROJECTS
This Python code is a Student Marks Analyzer. It collects student names and marks (0-100), stores them in a dictionary, and provides a continuous menu for calculations like Class Average, High/Low Marks, Pass/Fail Count, Passing Rate Percentage, and Individual Grades, until the user chooses to exit.
student_marks = {}

This Python script is an interactive command-line application designed to collect and analyze student marks for a class. It uses a dictionary to store student names and their corresponding marks (out of 100) and provides several analytical options, such as calculating the class average, finding the highest and lowest scores, determining pass/fail counts, calculating the passing rate, and assigning individual student grades.

✨ Features
Interactive Data Input: Prompts the user to enter the number of students, their names, and their marks.

Input Validation: Ensures marks are numeric and within the valid range of 0 to 100.

Menu-Driven Analysis: Offers a simple menu to perform various calculations on the collected data.

Statistical Analysis:

Calculate the Class Average.

Determine the Highest and Lowest Marks and the students who achieved them.

Count the Number of Students Passed/Failed (Pass threshold is 40).

Calculate the Passing Rate Percentage (Pass threshold is 40).

Grading System: Displays individual student grades based on the following scale:

Marks Range	Grade
90−100	A+
80−89	A
70−79	B
60−69	C
40−59	D
0−39	F

💻 How to Run the Script
Save the Code: Save the provided code into a file named, for example, student_analyzer.py.

Open Terminal: Open a terminal or command prompt.

Execute the Script: Run the script using the Python interpreter:

Bash

python student_analyzer.py
📋 Usage
The program will guide you through two main phases:

Phase 1: Data Entry
The script first asks for the total number of students you want to enter marks for.

For each student, it prompts for the name and their marks.

If the marks entered are not a number or are outside the 0-100 range, it will prompt you to enter valid input until successful.

Phase 2: Results Analysis Menu
After all marks are entered, the program displays the collected data and presents a menu:

Choice	Action
1	Calculate Class Average
2	Calculate The Highest/Lowest Marks
3	Calculate No. of Students Passed/Fail
4	Passing Rate Percentage
5	Display Individual Student Grades
6	Exit the program

Export to Sheets

You must enter a number between 1 and 6 to select an option. Selecting '6' will terminate the application.

⚙️ Code Structure
student_marks = {}: An empty dictionary used to store student names (keys) and marks (values).

Input Loops (while i < No_of_students and nested while True): Handles the data collection process, including robust error handling with a try-except ValueError block for non-numeric input and an if-else for mark range validation.

Main Menu Loop (while True): Controls the continuous presentation of the analysis options until the user chooses to exit. It also includes input validation for the menu choice.

Choice Blocks (elif choice == 1, elif choice == 2, etc.): Each block performs a specific calculation:

Choice 1 (Average): Uses sum() and division.

Choice 2 (High/Low): Uses max(), min(), and a list comprehension to find all students with the highest/lowest score.

Choice 3 & 4 (Pass/Fail): Uses a for-loop or a generator expression (sum(1 for...) to count students above the threshold of 40.

Choice 5 (Grades): Calls the nested function calculate_grade(marks) to assign a grade for each student.

📚 Dependencies
This script uses only standard Python 3 features and requires no external libraries.

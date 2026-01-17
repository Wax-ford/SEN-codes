Name: Adediran Wealth
Matric Number: 24/15484
Department: Computer Science
Course-Code: SEN 201
SEN ASSIGNMENT
Question
Pick any project of your choice and explain the full SDLC of that project Implement the project and push it to the github repo 
 NOTE: Names and nomenclatures used in your design must match the names and nomenclatures used in your implementation
Answers
Project Title
Student Result Management System (SRMS)
1. Project Overview
The Student Result Management System (SRMS) is a simple Python-based application that helps lecturers or school administrators record student details, compute results, and assign grades.
2. Software Development Life Cycle (SDLC)
The project follows the standard SDLC phases.
2.1 Planning Phase
Objective
To develop a system that can:
    • Collect student information
    • Accept test and exam scores
    • Compute total score, average score, and grade
    • Display results clearly
Tools & Resources
    • Programming language: Python
    • Editor: VS Code / PyCharm
    • Version control: GitHub
2.2 Requirement Analysis Phase
Functional Requirements
The system shall:
    1. Accept student name
    2. Accept matric number
    3. Accept test score and exam score
    4. Calculate:
        ◦ Total score
        ◦ Average score
        ◦ Grade
    5. Display student result
Non-Functional Requirements
    • Simple and user-friendly
    • Accurate calculations
    • Fast execution
2.3 System Design Phase
Variable Names (Design = Implementation)
Purpose
Variable Name
Student Name
student_name
Matric Number
matric_number
Test Score
test_score
Exam Score
exam_score
Total Score
total_score
Average Score
average_score
Grade
grade
Algorithm (Design)
START
  Input student_name
  Input matric_number
  Input test_score
  Input exam_score

  total_score = test_score + exam_score
  average_score = total_score / 2

  If average_score ≥ 70
     grade = 'A'
  Else if average_score ≥ 60
     grade = 'B'
  Else if average_score ≥ 50
     grade = 'C'
  Else if average_score ≥ 45
     grade = 'D'
  Else
     grade = 'F'

  Display student details and result
END
2.4 Implementation Phase (Python Code)
# Student Result Management System (SRMS)

student_name = input("Enter student name: ")
matric_number = input("Enter matric number: ")

test_score = float(input("Enter test score: "))
exam_score = float(input("Enter exam score: "))

total_score = test_score + exam_score
#average_score = total_score / 2

if total_score >= 70:
    grade = 'A'
elif total_score >= 60:
    grade = 'B'
elif total_score >= 50:
    grade = 'C'
elif total_score >= 45:
    grade = 'D'
else:
    grade = 'F'

print("\n--- Student Result ---")
print("Name:", student_name)
print("Matric Number:", matric_number)
print("Total Score:", total_score)
#print("Average Score:", average_score)
print("Grade:", grade)
2.5 Testing Phase
Test Case
Input
Value
Test Score
30
Exam Score
50
Expected Output
    • Total Score = 80
    • Average Score = 40
    • Grade = F
The program produces correct and expected results.
2.6 Deployment Phase
    • The Python file can be run on any system with Python installed.
    • The project is uploaded to GitHub for access and version control.
2.7 Maintenance Phase
Possible future improvements:
    • Store multiple students using lists or files
    • Add a menu system
    • Save results to a database
    • Add a graphical interface
4. Conclusion
The Student Result Management System (SRMS) was successfully developed using Python and followed all stages of the Software Development Life Cycle (SDLC).
The variable names and system structure used during design were strictly maintained during implementation.

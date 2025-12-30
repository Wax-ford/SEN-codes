# Student Result Management System (SRMS)

student_name = input("Enter student name: ")
matric_number = input("Enter matric number: ")

test_score = float(input("Enter test score: "))
exam_score = float(input("Enter exam score: "))

total_score = test_score + exam_score
average_score = total_score / 2

if average_score >= 70:
    grade = 'A'
elif average_score >= 60:
    grade = 'B'
elif average_score >= 50:
    grade = 'C'
elif average_score >= 45:
    grade = 'D'
else: grade = 'F'

print("\n----Student Result----")
print("Name:", student_name)
print("Matric Number:", matric_number)
print("Total Score:", total_score)
print("Average Score:", average_score)
print("Grade:", grade)
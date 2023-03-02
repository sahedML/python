
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# August 2022, Dhaka

# problem:
# Every student receives a grade in the inclusive range from to 1 to 100. Any less than 40 is a failing grade
# If the difference between the grade and the next multiple of is less than 5 and 3.
# Round grade up to the next multiple of 5. If the value of grade is less than 38 no rounding occurs
# as the result will still be a failing grade.
# solution:

# defining -our function which make grading system for the student marks
def gradingStudents(grades):
    for i in grades:
        if i < 38:
            print(i)
        elif i % 5 == 0:
            print(i)
        elif (i+1) % 5 == 0:
            print(i+1)
        elif (i+2) % 5 == 0:
            print(i+2)
        else:
            print(i)


# calling for the input value and function
if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    gradingStudents(grades)
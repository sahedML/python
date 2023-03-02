
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# July 2022, Dhaka

# problem:
# read in a dictionary containing key/value pairs of name:[marks] for a list of students.
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.
# solution:

# defining our function which will calculate the average marks of the students
def average_marks(student_marks, query_name):
    for name, scores in student_marks.items():
        if name == query_name:
            marks_sum = sum(scores)
            marks_len = len(scores)
            marks_avg = marks_sum / marks_len
            print("%.2f" % marks_avg)


# calling the function as _main_
if __name__ == '__main__':
    # variable n will take the number of students
    n = int(input())
    student_marks = {}
    for _ in range(n):
        # this input will take a student name and their subjects marks
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    # query_name variable will take the name of the student want to see his/her average marks
    query_name = input()

    average_marks(student_marks, query_name)


# solving HackerRank problems
# Sahed Ahmed Palash
# February 2023, Dhaka

# problem:
# A Discrete Mathematics professor has a class of students.
# Frustrated with their lack of discipline,
# the professor decides to cancel class if fewer than
# some number of students are present when class starts.
# Arrival times go from on time () to arrived late ().
# Given the arrival time of each student and a threshold number of attendees,
# determine if the class is cancelled.
# solution:

# defining the function which will print YES or NO
def angryProfessor():
    time = []
    for j in a:
        if j <= 0:
            time.append(1)
    if len(time) >= k:
        print("NO")
    elif len(time) < k:
        print("YES")


# calling the function as the main
if __name__ == "__main__":
    test_case = int(input().strip())
    for i in range(test_case):
        first_multiple_input = input().rstrip().split()
        n = first_multiple_input[0]
        k = int(first_multiple_input[1])
        a = list(map(int, input().rstrip().split()))
        angryProfessor()


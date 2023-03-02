# solving HackerRank problems
# Sahed Ahmed Palash
# February 2023, Dhaka

# problem:
# John Watson knows of an operation called a right circular
# rotation on an array of integers. One rotation operation
# moves the last array element to the first position and
# shifts all remaining elements right one. To test Sherlock's
# abilities, Watson provides Sherlock with an array of integers.
# Sherlock is to perform the rotation operation a number of times
# then determine the value of the element at a given position.
# For each array, perform a number of right circular rotations and
# return the values of the elements at the given indices.
# solution:

# defining the function which will calculate indices of list rotation
def circularArrayRotation():
    from collections import deque
    test_list = deque(a)
    test_list.rotate(k)
    test_list = list(test_list)
    for i in queries:
        print(test_list[i])


# calling the function as the main
if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    q = int(first_multiple_input[2])
    a = list(map(int, input().rstrip().split()))
    queries = []
    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)
    circularArrayRotation()

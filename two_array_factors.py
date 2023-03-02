
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# September 2022, Dhaka

# problem:
# There will be two arrays of integers
# Determine all integers that satisfy the following two conditions
# The elements of the first array are all factors of the integer being considered,
# The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays
# Determine how many such numbers exist
# solution:

# defining our function which will identify the factors and total number of factors in both arrays
def get_total_x(a, b):
    add = 0
    for i in range(1, 101):
        if all(i % x == 0 for x in a) and all(y % i == 0 for y in b):
            add += 1
    print(add)


# calling for the input value and function
if __name__ == '__main__':
    # input for number of integer in array 1 and array 2
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    # input for first array
    a = list(map(int, input().rstrip().split()))
    # input for second array
    b = list(map(int, input().rstrip().split()))
    get_total_x(a, b)
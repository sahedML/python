
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# July 2022, Dhaka

# problem:
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# solution:

# defining our function which will calculate the difference
def diagonal_difference(arr):
    pri_diag = 0
    sec_diag = 0
    for i in range(0, n):
        for j in range(0,n):
            if i == j:
                pri_diag += arr[i][j]

            if i == (n-j-1):
                sec_diag += arr[i][j]
    print(abs(pri_diag-sec_diag))


# calling the function as main
if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    diagonal_difference(arr)

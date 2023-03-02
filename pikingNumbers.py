# solving HackerRank problems
# Sahed Ahmed Palash
# December 2022, Dhaka

# problem:
# Given an array of integers,
# find the longest subarray where the absolute difference
# between any two elements is less than or equal to 1
# solution:

# defining the function which will find the longest subarray
def pickingNumbers():
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(n):
            if abs(a[j] - a[i]) <= 1:
                ans = max(ans, j - i + 1)
    print(ans)


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    pickingNumbers()

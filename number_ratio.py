
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# July 2022, Dhaka

# problem:
# calculate the ratios of its elements that are positive, negative, and zero
# solution:

# defining our function which will calculate the ratio of an element
def plus_minus(arr):
    post = 0
    neg = 0
    zero = 0
    for i in range(0, n):
        if arr[i] == 0:
            zero += 1
        elif arr[i]/abs(arr[i]) == 1:
            post += 1
        elif arr[i]/abs(arr[i]) == -1:
            neg += 1

    post = post/n
    neg = neg/n
    zero = zero/n

    print("%.6f" % post)
    print("%.6f" % neg)
    print("%.6f" % zero)


# calling for the input value and plus_minus function
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input(). rstrip().split()))
    plus_minus(arr)

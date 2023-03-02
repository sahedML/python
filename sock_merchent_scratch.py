# solving HackerRank problems
# Sahed Ahmed Palash
# October 2022, Dhaka

# problem:
# There is a large pile of socks that must be paired by color.
# Given an array of integers representing the color of each sock,
# determine how many pairs of socks with matching colors there are.
# Complete the sockMerchant function in the editor below.
# sockMerchant has the following parameter(s):
# int n: the number of socks in the pile
# int ar[n]: the colors of each sock
# Return int: the number of pairs
# solution:

# defining the function whihc will calculate the number of pairs
def sock_merchent(n, arr):
    x = set(arr)
    dup = []
    for c in x:
        if arr.count(c) > 1:
            indices = [i for i, x in enumerate(arr) if x == c]
            dup.append(indices)
    import math

    dup_sum = []
    for i in dup:
        if True:
            dup_sum.append(math.floor(len(i) / 2))
    print(sum(dup_sum))


# calling the input variable and function as __main__
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    sock_merchent(n, arr)


# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# September 2022, Dhaka

# problem:
# Given an array of integers and a positive integer k, determine the number of pairs (i, j),
# where i<j and i+j is divisible by k.
# solution:

# defining a function which will find the pairs (i, j)
def divisible_sum_pairs(n, k, arr, elements=None):
    pair_number = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if (arr[i]+arr[j]) % k == 0:
                pair_number += 1
    print(pair_number)


# calling the function as main
if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    divisible_sum_pairs(n, k, arr)





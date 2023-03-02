
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# August 2022, Dhaka

# problem:
# calculate the length of a non-divisible-subset
# solution:

# defining -our function which will calculate the length of subset
def non_divisible_subset(k, s):
    s1 = round(n/2)
    subset1 = (s[:s1])
    print(subset1)
    subset2 = (s[s1:])
    print(subset2)
    sum1 = sum(subset1)
    print(sum1)
    sum2 = sum(subset2)
    print(sum2)
    if sum1/k == 0:
        print(len(sum1))
    elif sum2/k == 0:
        print(len(sum2))


# calling for the input value and function
if __name__ == "__main__":
    firstMultipleInput = input().rstrip().split()
    n = int(firstMultipleInput[0])
    k = int(firstMultipleInput[1])
    s = list(map(int, input().rstrip().split()))
    non_divisible_subset(k, s)

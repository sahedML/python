
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# July 2022, Dhaka

# problem:
# in this challenge, you are required to calculate and print the sum of the elements in an array
# keeping in mind that some of those integers may be quite large.
# solution:

# defining our function to calculate the sum of an array
def very_big_sum(ar):
    bigSum = []
    for i in ar:
        bigSum.append(i)
    print(sum(bigSum))


# calling our input and function as _main_
if __name__ == '__main__':
    # total number of an array
    ar_count = int(input().strip())
    # array of integers
    ar = list(map(int, input().rstrip().split()))
    very_big_sum(ar)
    

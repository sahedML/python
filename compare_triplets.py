
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# July 2022, Dhaka

# problem:
# given two triplets, compare each one in same position, award points for comparison winner.
# sum up points for the triplets. print each triplet total points
# solution:

# defining our function to calculate sum for each triplets
def compare_triplets(a, b):
    a_score = []
    b_score = []
    for i in range(len(a)):
        if a[i] > b[i]:
            a_score.append(1)
            b_score.append(0)
        elif a[i] == b[i]:
            a_score.append(0)
            b_score.append(0)
        else:
            b_score.append(1)
            a_score.append(0)
    a_score = sum(a_score)
    b_score = sum(b_score)
    print(a_score, b_score)


# calling our input and function as _main_
if __name__ == '__main__':
    # total number of an integer
    a = list(map(int, input().rstrip().split()))
    # integers
    b = list(map(int, input().rstrip().split()))
    compare_triplets(a, b)

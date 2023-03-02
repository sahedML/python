
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# September 2022, Dhaka

# problem:
# Given an array of bird sightings where every element represents a bird type id,
# The first line contains an integer n, the size of arr.
# The second line describes arr as n space-separated integers, each a type number of the bird sighted.
# determine the id of the most frequently sighted type.
# If more than 1 type has been spotted that maximum amount, return the smallest of their ids.
# solution:

# defining a function which calculate the maximum number of bird type
def bird_type(id):
    count = [0] * 6
    for i in id:
        count[i] += 1
    print(count.index(max(count)))


# calling the input values and bird_type
if __name__ == "__main__":
    # input value of array length
    n = int(input().strip())
    # input value of an array for birds id
    id = list(map(int, input().rstrip().split()))
    bird_type(id)





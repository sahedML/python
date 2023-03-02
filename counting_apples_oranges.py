
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# August 2022, Dhaka

# problem:
# Given a person house whose house length is between variables s and t,
# and we have two trees, one is apple other one is orange.
# Since we have been given some distance of the fallen apple, and oranges respectively,
# what we have to do is to find those apples, and oranges whose distance falls in between the s and t,
# or I must say which falls on xyz person's house.
# solution:

# defining our function which will calculate apples and orages fall on the house
def count_apples_and_oranges(s, t, a, b, apples, oranges):
    print(sum([1 for x in apples if (x+a) >= s and (x + a) <= t]))
    print(sum([1 for x in oranges if (x+b) >= s and (x + b) <= t]))

# calling for the input value and function
if __name__ == '__main__':
    # input for house starting and end point
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    # input for apple and orange tree position
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    # input for
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    count_apples_and_oranges(s, t, a, b, apples, oranges)

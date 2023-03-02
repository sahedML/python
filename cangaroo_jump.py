
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# September 2022, Dhaka

# problem:
# You are choreographing a circus show with various animals. For one act, you are
# given two kangaroos on a number line ready to jump in the positive direction.
# The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
# The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same
# time as part of the show.
# If it is possible, return YES, otherwise return NO.
# solution:

# defining our function which will calculate the precise position of Kangaroo and print a string (Yes/No)
def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 > v1:
        print("NO")
    else:
        if v2 - v1 == 0:
            print("NO")
        else:
            result = (x1 - x2) % (v2 - v1)
            if result == 0:
                print("YES")
            else:
                print("NO")

# calling for the input value and function
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    kangaroo(x1, v1, x2, v2)

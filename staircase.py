
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# July 2022, Dhaka

# problem:
# Print a staircase of size using # symbols and spaces.
# The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of .
# solution:

# defining our function which will print a staircase
def staircase(n):
    for i in range(1, n+1):
        for j in range(n, 0, -1):
            if j > i:
                print(" ", end="")
            else:
                print("#", end="")
        print(" ")


# calling an input value and staircase function
if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)

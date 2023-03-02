
# solving HackerRank python problems
# Sahed Ahmed Palash
# December 2022, Dhaka

# problem:
# Mr. Vincent works in a door mat manufacturing company.
# One day, he designed a new door mat with the following specifications:
# Mat size must be NXM. (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |,. and - characters.
# solution:

# defining the function which will create a designer doormat
def doorMat():
    for i in range(1, N, 2):
        print((i * ".|.").center(M,"-"))
    print("WELCOME".center(M, "-"))
    for i in range(N-2, -1, -2):
        print((i * ".|.").center(M, "-"))


# calling the function as main:
if __name__ == "__main__":
    N, M = map(int, input().split())
    doorMat()


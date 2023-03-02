
# solving HackerRank problems
# Sahed Ahmed Palash
# February 2023, Dhaka

# problem:
# A video player plays a game in which the character competes in a hurdle race.
# Hurdles are of varying heights, and the characters have a maximum height they can jump.
# There is a magic potion they can take that will increase their maximum jump height
# by  unit for each dose.
# How many doses of the potion must the character take to be able to jump all the hurdles.
# If the character can already clear all the hurdles, return .
# solution:

# defining the function which will determine the doses of potion
def hurdleRace():
    max_height = max(height)
    if k < max_height:
        print(max_height-k)
    else:
        print(0)


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    height = list(map(int, input().rstrip().split()))
    hurdleRace()

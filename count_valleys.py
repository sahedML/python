
# solving HackerRank problems
# Sahed Ahmed Palash
# October 2022, Dhaka

# problem:
# An avid hiker keeps meticulous records of their hikes.
# During the last hike that took exactly number of steps, for every step
# it was noted if it was an uphill, U , or a downhill, D step.
# Hikes always start and end at sea level, and each step up or down represents a
# unit change in altitude. We define the following terms:
# A mountain is a sequence of consecutive steps above sea level,
# starting with a step up from sea level and ending with a step-down to sea level.
# A valley is a sequence of consecutive steps below sea level,
# starting with a step-down from sea level and ending with a step-up to sea level.
# Given the sequence of up and down steps during a hike,
# find and print the number of valleys walked through.
# solution:

# defining the function which will calculate the number of valleys
def countingValleys(steps, path):
    base = 0
    valley = 0
    for i in range(len(path)):
        if path[i] == "U":
            base += 1
            if base == 0:
                valley += 1
        else:
            base -= 1
    print(valley)


# calling the function as main
if __name__ == '__main__':
    steps = int(input().strip())
    path = input()
    countingValleys(steps, path)

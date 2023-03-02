# solving HackerRank problems
# Sahed Ahmed Palash
# February 2023, Dhaka

# problem:
# A jail has a number of prisoners and a number of treats to pass out to them.
# Their jailer decides the fairest way to divide the treats is to seat the prisoners around
# a circular table in sequentially numbered chairs. A chair number will be drawn from a hat.
# Beginning with the prisoner in that chair, one candy will be handed to each prisoner
# sequentially around the table until all have been distributed.
# The jailer is playing a little joke, though. The last piece of candy looks like all the others,
# but it tastes awful. Determine the chair number occupied by the prisoner who will receive that candy.
# solution:

# defining the function which will determine the chair number
def saveThePrisoner():
    pos = (s - 1 + m % n) % n
    if pos == 0:
        print(n)
    else:
        print(pos)


# calling the function as the main
if __name__ == "__main__":
    t = int(input().rstrip())
    for i in range(t):
        multiple_input = input().rstrip().split()
        n = int(multiple_input[0])
        m = int(multiple_input[1])
        s = int(multiple_input[2])
        saveThePrisoner()

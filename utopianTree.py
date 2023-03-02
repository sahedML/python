
# solving HackerRank problems
# Sahed Ahmed Palash
# February 2023, Dhaka

# problem:
# The Utopian Tree goes through 2 cycles of growth every year.
# Each spring, it doubles in height. Each summer, its height increases by 1 meter.
# A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring.
# How tall will the tree be after  growth cycles?
# solution:

# defining the function which will calculate the height of Utopian Tree
def utopianTree():
    h = 1
    for i in range(1, n + 1):
        if i % 2 != 0:
            h *= 2
        else:
            h += 1
    print(h)


# calling the designerPDFViewer function as the main
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        utopianTree()

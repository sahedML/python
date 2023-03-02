
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# July 2022, Dhaka

# Problem: based on the given inputs, print all the permutations and their possible coordinates

# solution:

# defining our function to calculate possible permutations and their coordinates
def per_cord(x, y, z, n):
    i = [i for i in range(0, x + 1)]
    j = [i for i in range(0, y + 1)]
    k = [i for i in range(0, z + 1)]
    per = [[m, n, o] for m in i for n in j for o in k]
    possible_coordinates = [i for i in per if sum(i) != n]
    print(per)
    print(possible_coordinates)


# calling the inputs and function as _main_
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    per_cord(x, y, z, n)




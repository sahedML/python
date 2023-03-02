
# solving HackerRank problems
# Sahed Ahmed Palash
# October 2022, Dhaka

# problem:
# A person wants to determine the most expensive computer keyboard and USB drive
# that can be purchased with a give budget.
# Given price lists for keyboards and USB drives and a budget, find the cost to buy them.
# If it is not possible to buy both items, return -1 .
# solution:

# defining the function which will calculate the cost
def get_money_spent(keyboards, drives, b):
    list = []
    for i in keyboards:
        for j in drives:
            if (i+j) <= b:
                list.append(i+j)
    if not list:
        print(-1)
    else:
        print(max(list))


# calling the input variable and function
if __name__ == '__main__':
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    get_money_spent(keyboards, drives, b)

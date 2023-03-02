
# solving HackerRank problems
# Sahed Ahmed Palash
# October 2022, Dhaka

# problem:
# Two friends Anna and Brian, are deciding how to split the bill at a dinner.
# Each will only pay for the items they consume.
# Brian gets the check and calculates Anna's portion.
# You must determine if his calculation is correct.
# For example, assume the bill has the following prices: bill = [2, 4, 6]
# Anna declines to eat item k = bill[2] which costs 6.
# If Brian calculates the bill correctly, Anna will pay (2+4)/2=3.
# If he includes the cost of bill[2], he will calculate (2+4+6)/2=6.
# In the second case, he should refund to Anna.
# Complete the bonAppetit function.
# It should print "Bon Appetit" if the bill is fairly split.
# Otherwise, it should print the integer amount of money that Brian owes Anna.
# bonAppetit has the following parameter(s):
# bill: an array of integers representing the cost of each item ordered
# k: an integer representing the zero-based index of the item Anna doesn't eat
# b: the amount of money that Anna contributed to the bill
# solution:

# defining the function which calculate the exact bill
def bon_appetit(bill, k, b):
    actual_bill = bill
    del actual_bill[k]
    anna_bill = sum(actual_bill)/2
    brian_bill = sum(bill)/2+bill[k]
    if anna_bill == b:
        print("Bon Appetit")
    else:
        print(int(b-anna_bill))

# calling the function as __main__
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bon_appetit(bill, k, b)



# solving HackerRank problems
# Sahed Ahmed Palash
# February 2023, Dhaka

# problem:
# Lily likes to play games with integers.
# She has created a new game where she determines the difference
# between a number and its reverse. For instance, given the number 12,
# its reverse is 21. Their difference is 9. The number  120 reversed is 21 ,
# and their difference is 99.
# She decides to apply her game to decision-making.
# She will look at a numbered range of days and will only go to a movie on a beautiful day.
# Given a range of numbered days, [i....j] and a number k,
# determine the number of days in the range that are beautiful.
# Beautiful numbers are defined as numbers where i-reverse[i] is evenly divisible by k .
# If a day's value is a beautiful number, it is a beautiful day.
# Return the number of beautiful days in the range.
# solution:

# defining the function which will determine the number of beautiful days
def beautifulDays():
    count = 0
    for items in range(i, j+1):
        if abs(not(items - int(str(items)[::-1])) % k):
            count += 1
    print(count)


# calling the function as the main
if __name__ == "__main__":
    multiple_input = input().rstrip().split()
    i = int(multiple_input[0])
    j = int(multiple_input[1])
    k = int(multiple_input[2])
    beautifulDays()

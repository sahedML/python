
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# September 2022, Dhaka

# problem:
# Print the full date of Day of the Programmer during year y in the format dd.mm.yyyy,
# where dd is the two-digit day, mm is the two-digit month, and yyyy is y .
# solution:

# defining our function which will find the 256th day of the year
def day_of_programmer(y):
    leap_year_count_gregorian = 0
    if 1918 < y <= 2700:
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
            leap_year_count_gregorian = 1
        if leap_year_count_gregorian == 1:
            print("12.09." + str(y))
        else:
            print("13.09." + str(y))

    leap_year_count_julian = 0
    if 1700 <= y < 1918:
        if y % 4 == 0:
            leap_year_count_julian = 1
        if leap_year_count_julian == 1:
            print("12.09." + str(y))
        else:
            print("13.09." + str(y))

    if y == 1918:
        print("26.09.1918")


# calling the function as main
if __name__ == "__main__":
    y = int(input().strip())
    day_of_programmer(y)

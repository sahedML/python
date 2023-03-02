
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# August 2022, Dhaka

# problem:
# given a time in -hour AM/PM format, convert it to military (24-hour) time.
# solution:

# defining -our function which will convert user defined time to 24 hours time
def time_conversion(userTime):
    if userTime[-2:] == "AM" and userTime[:2] == "12":
        return "00" + userTime[2:-2]

    elif userTime[-2:] == "AM":
        return userTime[:-2]

    elif userTime[-2:] == "PM" and userTime[:2] == "12":
        return userTime[:-2]

    else:
        return str(int(userTime[:2]) + 12) + userTime[2:-2]


# calling for the input value and function
if __name__ == "__main__":
    # take time as input
    userTime = input()
    time_conversion(userTime)
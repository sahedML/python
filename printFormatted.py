# solving HackerRank python problems
# Sahed Ahmed Palash
# December 2022, Dhaka

# problem:
# Given an integer, n, print the following values for each integer i from 1 to n:
# 1. Decimal
# 2. Octal
# 3. Hexadecimal (capitalized)
# 4. Binary
# Function Description
# Complete the print_formatted function in the editor below.
# print_formatted has the following parameters:
# int number: the maximum value to print
# Prints
# The four values must be printed on a single line in the order
# specified above for each i from 1 to number. Each value should be space-padded
# to match the width of the binary value of number and the values should be separated by a single space.
# solution:

# defining the function which will create a designer mat
def printFormatted():
    padding = n.bit_length()
    for i in range(1, n+1):
        print(str(i).rjust(padding),
              oct(i).split("o")[1].rjust(padding),
              hex(i).split("x")[1].upper().rjust(padding),
              bin(i).split("b")[1].rjust(padding))


# calling the function as main:
if __name__ == "__main__":
    n = int(input().rstrip())
    printFormatted()

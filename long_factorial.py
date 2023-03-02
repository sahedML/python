
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# July 2022, Dhaka

# problem:
# calculate the factorial of a given number
# solution:

# defining -our function which will calculate the factorial of a number
def long_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact*i
    print(fact)


# calling for the input value and function
if __name__ == "__main__":
    n = int(input().strip())
    long_factorial(n)
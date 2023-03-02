
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# September 2022, Dhaka

# problem:
# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
# Lily decides to share a contiguous segment of the bar selected such that:
# The length of the segment matches Ron's birth month, and,
# The sum of the integers on the squares is equal to his birthday.
# Determine how many ways she can divide the chocolate.
# birthday has the following parameter(s):
# int s[n]: the numbers on each of the squares of chocolate
# int d: Ron's birthday
# int m: Ron's birth month
# Returns int: the number of ways the bar can be divided
# solution:

# defining our function which will find the number of ways the bar can be divided
def birthday(s, d, m):
    ans = 0
    for i in range(n-m+1):
        if sum(s[i:i+m]) == d:
            ans += 1
    print(ans)


# calling for the input value and function
if __name__ == '__main__':
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    first_multiple_input = input().rstrip().split()
    d = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    birthday(s, d, m)

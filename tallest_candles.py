
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# August 2022, Dhaka

# problem:
# calculate tallest candles
# solution:

# defining -our function which will calculate the tallest candles
def birthday_cake_candles(ar):
    c = 0
    temp = max(ar)
    for i in range(0, len(ar)):
        if ar[i] == temp:
            c = c + 1
    print(c)


# calling for the input value and function
if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    birthday_cake_candles(ar)


# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# July 2022, Dhaka

# problem:
# given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score.

# solution:

# defining our function to calculate the runner-up
def runner_up(n, score, score_list):
    x = max(score_list)
    y = -99999
    for i in range(0, n):
        if x > score_list[i] > y:
            y = score_list[i]
    print(y)


# calling the input values and runner-up function as _main_
if __name__ == "__main__":
    n = int(input())
    score = map(int, input().split())
    score_list = list(score)
    runner_up(n, score, score_list)





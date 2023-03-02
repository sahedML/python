
# solving HackerRank problems
# Sahed Ahmed Palash
# February 2023, Dhaka

# problem:
# An arcade game player wants to climb to the top of the leaderboard
# and track their ranking.
# The game uses Dense Ranking, so its leaderboard works like this:
# The player with the highest score is ranked number 1 on the leaderboard.
# Players who have equal scores receive the same ranking number,and
# the next player(s) receive the immediately following ranking number.
# solution:

# defining the function which will determine the leaderboard
def climbingLeaderboard():
    from collections import Counter
    import bisect
    counts = Counter(ranked)
    counts = sorted(counts)
    ranked_count = len(counts)
    for a in player:
        i = bisect.bisect_left(counts, a)
        if i < ranked_count and counts[i] == a:
            print(ranked_count - i)
        else:
            print(ranked_count + 1 - i)


# calling the function as main
if __name__ == '__main__':
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    climbingLeaderboard()

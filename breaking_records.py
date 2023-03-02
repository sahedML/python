
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# September 2022, Dhaka

# problem:
# Maria plays college basketball and wants to go pro. Each season she maintains a record of her play.
# She tabulates the number of times she breaks her season record for most points and least points in a game.
# Points scored in the first game establish her record for the season, and she begins counting from there.
# Return an array with the numbers of times she broke her records. Index 0 is for breaking most points records,
# and index 1 is for breaking least points records.
# solution:

# defining our function which will find the most and least record breaking scores
def breaking_records(scores):
    # variable
    high = scores[0]
    low = scores[0]
    # counter
    high_number = 0
    low_number = 0
    for i in range(1, len(scores)):
        if scores[i] > high:
            high_number += 1
            high = scores[i]
        if scores[i] < low:
            low_number += 1
            low = scores[i]
    print(high_number, low_number)


# calling for the function as main
if __name__ == '__main__':
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    breaking_records(scores)


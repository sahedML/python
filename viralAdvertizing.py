
# solving HackerRank problems
# Sahed Ahmed Palash
# February 2023, Dhaka

# problem:
# HackerLand Enterprise is adopting a new viral advertising strategy.
# When they launch a new product, they advertise it to exactly 5 people on social media.
# On the first day, half of those 5 people (i.e., floor(5/2)==2) like the advertisement and
# each shares it with 3 of their friends. At the beginning of the second day, floor(5/2)*3==2*3==6
# people receive the advertisement.
# Each day, floor(recipient/2) of the recipients like the advertisement and will share it with 3
# friends on the following day. Assuming nobody receives the advertisement twice,
# determine how many people have liked the ad by the end of a given day,
# beginning with launch day as day 1.
# solution:

# defining the function which will determine how many people liked the advertisement
def viralAdvertisement():
    import math
    shared = 5
    likes = 2
    cum_likes = 2
    for i in range(1, n):
        shared = math.floor(shared/2)*3
        likes = math.floor(shared/2)
        cum_likes += likes
    print(cum_likes)


# calling the function as the main
if __name__ == "__main__":
    n = int(input().rstrip())
    viralAdvertisement()

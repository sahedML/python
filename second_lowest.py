
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# July 2022, Dhaka

# problem:
# given a list of participants' name and score,
# you are required to find the second-lowest value.
# solution:

# defining our function to calculate the second-lowest value
def second_lowest(stu_list):
    stu_list.sort(key=lambda x: x[1])
    the_min = min([l[1] for l in stu_list])
    stu_list = list(filter(lambda x: x[1] > the_min, stu_list))
    sec_min = min(stu_list, key=lambda x: x[1])
    a = []
    minimum = sec_min[1]
    for i in stu_list:
        if i[1] == minimum:
            a.append(i[0])
    a.sort()
    for i in a:
        print(i)


# calling the input value and our function as _main_
if __name__ == '__main__':
    stu_list = []
    for i in range(int(input())):
        name = str(input())
        score = float(input())
        stu_list.append([name, score])

    second_lowest(stu_list)
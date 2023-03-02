
# solving HackerRank "coding challenge" problems
# Sahed Ahmed Palash
# August 2022, Dhaka

# problem:
# initiate list commands based on user defined input
# solution:

# defining our function which will execute user defined commands for the list
def list_functions(N):
    lst = []
    for i in range(0, N):
        cmd = input().split()
        if cmd[0] == "insert":
            lst.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "append":
            lst.append(int(cmd[1]))
        elif cmd[0] == "print":
            print(lst)
        elif cmd[0] == "remove":
            lst.remove(int(cmd[1]))
        elif cmd[0] == "sort":
            lst.sort()
        elif cmd[0] == "pop":
            lst.pop()
        else:
            lst.reverse()


# calling for the input value and function
if __name__ == "__main__":
    N = int(input())
    list_functions(N)
import sys

N, M = map(int,sys.stdin.readline().split())
selected = []
def dfs():

    if M == len(selected):
        for num in selected:
            print(num, end=" ")
        print()

    for i in range(1,N+1):
        if i not in selected:
            selected.append(i)
            dfs()
            selected.remove(i)

dfs()
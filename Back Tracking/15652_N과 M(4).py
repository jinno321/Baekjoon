import sys

N, M = map(int, sys.stdin.readline().split())
selected = []


def dfs(start):
    if M == len(selected):
        for num in selected:
            print(num, end=" ")
        print()
        return

    for i in range(start, N + 1):
        selected.append(i)
        dfs(i)
        selected.remove(i)

dfs(1)

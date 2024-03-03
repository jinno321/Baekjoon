import sys

N, M = map(int, sys.stdin.readline().split())
selected = []


def dfs(start):
    if len(selected) == M:
        for i in range(len(selected)):
            print(selected[i], end = " ")
        print()
        return

    for i in range(start, N + 1):
        if i not in selected:
            selected.append(i)
            dfs(i + 1)
            selected.pop()


dfs(1)

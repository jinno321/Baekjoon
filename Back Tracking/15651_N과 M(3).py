import sys

N, M = map(int, sys.stdin.readline().split())
stack = []


def dfs():
    if len(stack) == M:
        for i in stack:
            print(i, end=" ")
        print()
        return

    for i in range(1,N+1):
        stack.append(i)
        dfs()
        stack.pop()

dfs()

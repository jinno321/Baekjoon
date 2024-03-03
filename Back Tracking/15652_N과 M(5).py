import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
stack = []
arr.sort()


def dfs():
    if len(stack) == M:
        for num in stack:
            print(num, end=" ")
        print()
        return

    for i in range(N):
        if arr[i] not in stack:
            stack.append(arr[i])
            dfs()
            stack.remove(arr[i])

dfs()

import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
stack = []
arr.sort()


def dfs(start):
    if len(stack) == M:
        for num in stack:
            print(num, end=" ")
        print()
        return

    for i in range(start,N):
        stack.append(arr[i])
        dfs(i)
        stack.remove(arr[i])

dfs(0)

import sys

n, k = list(map(int, sys.stdin.readline().split()))

arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

dp = [[-1 for i in range(k + 1)] for _ in range(n)]
count = 0


def function(i, j):
    global n
    global k

    if i == 0:
        if j % arr[i] == 0:
            return 1
        else:
            return 0

    if j - arr[i] >= 0:
        if dp[i][j - arr[i]] == -1: dp[i][j - arr[i]] = function(i, j - arr[i])
        if dp[i - 1][j] == -1: dp[i - 1][j] = function(i - 1, j)
        return dp[i][j - arr[i]] + dp[i - 1][j]
    else:
        if dp[i - 1][j] == -1: dp[i - 1][j] = function(i - 1, j)
        return dp[i - 1][j]


print(function(n - 1, k))

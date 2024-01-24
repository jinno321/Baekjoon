import sys

n = int(input())
arr = [[] for _ in range(n)]
dp = [[0 for i in range(n)] for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))

dp[0][0] = arr[0][0]
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = arr[i][j] + dp[i - 1][j]
        else:
            dp[i][j] = arr[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[n-1]))
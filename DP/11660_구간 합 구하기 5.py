import sys

N, K = map(int, sys.stdin.readline().split())
arr = [[0 for row in range(N + 1)] for col in range(N + 1)]
dp = [[0 for row in range(N + 1)] for col in range(N + 1)]
for i in range(1, N + 1):
    arr[i] =[0]+ (list(map(int, sys.stdin.readline().split())))

dp[1][1] = arr[1][1]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + arr[i][j]
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1-1])

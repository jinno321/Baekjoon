import sys

T = int(input())

for i in range(T):
    n = int(input())
    arr = [[0 for j in range(n)] for _ in range(2)]
    dp = [[0 for j in range(n)] for _ in range(2)]

    for j in range(2):
        arr[j] = list(map(int, sys.stdin.readline().split()))

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if n>1:
        dp[0][1] = arr[1][0] + arr[0][1]
        dp[1][1] = arr[0][0] + arr[1][1]

    for x in range(2, n):
        dp[0][x] = max(dp[1][x - 2], dp[1][x - 1]) + arr[0][x]
        dp[1][x] = max(dp[0][x - 2], dp[0][x - 1]) + arr[1][x]

    print(max(dp[0][n - 1], dp[1][n - 1]))

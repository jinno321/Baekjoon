import sys

N = int(input())
dp = [0 for _ in range(N)]

dp[0] = 1

for i in range(1,N):
    if i == 1:
        dp[1] = 1
    else:
        dp[i] = dp[i-1]+dp[i-2]

print(dp[N-1])

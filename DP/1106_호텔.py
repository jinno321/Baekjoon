import sys

C, N = map(int, sys.stdin.readline().split())
cost_list = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp = [1e7 for _ in range(C + 100)]
dp[0] = 0

for cost, num_customer in cost_list:
    for i in range(num_customer, C + 100):
        dp[i] = min(dp[i - num_customer] + cost, dp[i])

print(min(dp[C:]))
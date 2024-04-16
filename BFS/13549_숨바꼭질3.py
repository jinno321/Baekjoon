import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())

dp = [-1] * 200001
arr = deque()
dp[N] = 0

arr.append(N)

while arr:
    num = arr.popleft()
    if num == K:
        print(dp[K])
        break
    if 0<=num * 2 < 200001 and dp[num*2] == -1:
        dp[num * 2] = dp[num]
        arr.appendleft(num * 2)
    if 0<=num + 1 < 200001 and dp[num+1] == -1:
        dp[num + 1] = dp[num] + 1
        arr.append(num + 1)
    if 0<=num-1 < 200001 and  dp[num-1] == -1:
        dp[num - 1] = dp[num] + 1
        arr.append(num - 1)





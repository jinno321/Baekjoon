N = int(input())
arr = [0 for _ in range(N)]
dp = [0 for _ in range(N)]

for i in range(N):
    arr[i] = int(input())

dp[0] = arr[0]
for i in range(1,N):
    if i == 1:
        dp[1] = arr[0]+arr[1]
    elif i == 2:
        dp[2] = max(arr[i-2]+arr[i], arr[i-2]+arr[i-1],arr[i-1]+arr[i])
    else:
        dp[i] = max(arr[i] + dp[i-2],arr[i]+arr[i-1]+dp[i-3],dp[i-1])

print(dp[N-1])
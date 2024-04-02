import sys
import math

C, N = map(int, sys.stdin.readline().split())
answer = float("inf")
arr = [] * N


for _ in range(N):
    cost, cust = map(int, sys.stdin.readline().split())
    arr.append((cost/cust,cost, cust))

arr.sort()
restcust = C
nowcost = 0
for i in range(N):
    if restcust % arr[i][2] == 0:
        answer = min(answer, nowcost + arr[i][1]*(restcust // arr[i][2]))
        break
    answer = min(answer, nowcost + arr[i][1] * (restcust // arr[i][2]+1))
    nowcost += ((restcust // arr[i][2]) * arr[i][1])
    restcust = restcust % arr[i][2]


print(answer)

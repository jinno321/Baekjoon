import sys

N = int(input())
arr = [0,0,0]

High = [0, 0, 0]
Low = [0, 0, 0]
Xhigh = [0,0,0]
Xlow = [0,0,0]
for k in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    if k == 0:
        High = arr.copy()
        Low = arr.copy()
        Xhigh = High.copy()
        Xlow = arr.copy()
    else:
        High[0] = max(Xhigh[0], Xhigh[1]) + arr[0]
        High[1] = max(Xhigh[0], Xhigh[1], Xhigh[2]) + arr[1]
        High[2] = max(Xhigh[1], Xhigh[2]) + arr[2]
        Xhigh = High.copy()
        Low[0] = min(Xlow[0], Xlow[1]) + arr[0]
        Low[1] = min(Xlow[0], Xlow[1], Xlow[2]) + arr[1]
        Low[2] = min(Xlow[1], Xlow[2]) + arr[2]
        Xlow = Low.copy()

print(max(High),min(Low))

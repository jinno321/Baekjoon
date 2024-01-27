import sys
import heapq

N = int(input())
PQ = []
arr = [[] for _ in range(N)]

for i in range(N):
    dead, ramen = list(map(int, sys.stdin.readline().split()))
    tem = [ramen, dead]
    arr[i] = tem

arr.sort(key=lambda x: x[1])
count = 1
answer = 0
idx = 0
while idx < N:
    while arr[idx][1] <= count:
        heapq.heappush(PQ, arr[idx])
        idx += 1
    if len(PQ) == 0: continue
    node = heapq.heappop(PQ)
    print(node)
    answer += node[0]
    count += 1
print(answer)

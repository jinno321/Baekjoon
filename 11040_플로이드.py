import sys
import heapq

queue = []

N = int(input())
M = int(input())
Graph = [[] for i in range(N + 1)]  # adjency List

for i in range(M):
    fr, to, weight = map(int, sys.stdin.readline().split())
    Graph[fr].append([to, weight])


def Dijkstra(start):
    global Graph
    time = [int(1e10)] * (N + 1)
    heapq.heappush(queue,[0,start])
    time[start] = 0

    while queue:
        weight,node = queue.pop()
        for n,w in Graph[node]:
            if weight + w < time[n]:
                time[n] = weight + w
                heapq.heappush(queue,[weight+w,n])

    return time


for start in range(1,N + 1):
    time = Dijkstra(start)
    for t in range(1,len(time)):
        if time[t] == int(1e10):
            print(0, end =" ")
        else: print(time[t], end=" ")
    print()

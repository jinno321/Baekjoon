import sys

sys.setrecursionlimit(10 ** 7)

start = 0
flag = 0


def DFS(x, wei):
    for i in Graph[x]:
        a, b = i
        if visited[a] == -1:
            visited[a] = wei + b
            DFS(a, wei + b)


N = int(input())
Graph = [[] for _ in range(N + 1)]
for _ in range(N):
    line = list(map(int, input().split()))
    cnt_node = line[0]
    idx = 1
    while line[idx] != -1:
        adj_node, adj_cost = line[idx], line[idx+1]
        Graph[cnt_node].append((adj_node, adj_cost))
        idx += 2


visited = [-1] * (N + 1)
visited[1] = 0
DFS(1,0)

start = visited.index(max(visited))
visited = [-1] * (N + 1)
visited[start]=0
DFS(start,0)

print(max(visited))

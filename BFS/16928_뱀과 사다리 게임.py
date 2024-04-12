import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [i for i in range(101)]
visited = [0 for _ in range(101)]

for _ in range(N + M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start] = end

queue = deque()
queue.append(1)

while queue:
    num = queue.popleft()
    for i in range(1, 7):
        dice = i + num

        if dice > 100: continue

        if visited[graph[dice]] == 0:
            visited[graph[dice]] = visited[graph[num]] + 1
            queue.append(graph[dice])

        if dice == 100: break

print(visited[100])
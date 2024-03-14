import sys
from collections import deque

col, row = map(int, sys.stdin.readline().split())
arr = [[0 for row in range(row)] for col in range(col)]
visited = [[-1 for row in range(row)] for col in range(col)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

queue = deque()
for i in range(col):
    arr[i] = list(map(int, sys.stdin.readline().split()))
    if 2 in arr[i]:
        (y,x) = (i,arr[i].index(2))
        queue.append((y,x))
        visited[y][x] = 0


while queue:
    y, x = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < row and 0 <= ny < col and visited[ny][nx] == -1 and arr[ny][nx] != 0:
            visited[ny][nx] = visited[y][x] + 1
            queue.append((ny,nx))

for i in range(col):
    for j in range(row):
        if arr[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=" ")
    print()

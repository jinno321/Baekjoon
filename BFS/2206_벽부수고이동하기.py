import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
queue = deque()
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
count = 1
answer = -1
arr = [0 for _ in range(N)]
visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]

for i in range(N):
    arr[i] = list(sys.stdin.readline().strip())

queue.append([0, 0, 0])
visit[0][0][0] = 1

while queue:
    x, y, w = queue.popleft()
    if x == M - 1 and y == N - 1:
        answer = visit[y][x][w]
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            #다음 칸을 갈 수 있고, 방문하지 않았을 떄
            if arr[ny][nx] == '0' and visit[ny][nx][w] == 0:
                visit[ny][nx][w] = visit[y][x][w] + 1
                queue.append([nx, ny, w])
            #다음 칸을 갈 수 없지만 벽 뚫기 찬스를 사용하지 않았을때
            elif arr[ny][nx] == '1' and w == 0:
                visit[ny][nx][w + 1] = visit[y][x][w] + 1
                queue.append([nx, ny, w + 1])

print(answer)

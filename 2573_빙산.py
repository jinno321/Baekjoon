import collections

N, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = collections.deque()
day = 0
check = False


def bfs(a, b):
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < m:
                if graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif graph[nx][ny] == 0:
                    count[x][y] += 1
    return 1

while True:
    visited = [[False] * m for _ in range(N)]
    count = [[0] * m for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == False:
                result.append(bfs(i, j))

    for i in range(N):
        for j in range(m):
            graph[i][j] -= count[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    if len(result) == 0:
        break
    if len(result) >= 2:  # 빙산이 분리되면 break
        check = True
        break
    day += 1

if check:
    print(day)
else:
    print(0)
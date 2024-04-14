import sys
sys.setrecursionlimit(10**5)

N, M = map(int, sys.stdin.readline().split())

Graph = [[0 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = 0


def DFS(x, y, visited, Graph):
    visited[x][y] += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if Graph[nx][ny] == 1:
                visited[nx][ny] += 1
            if Graph[nx][ny] == 0 and visited[nx][ny] == 0:
                DFS(nx, ny, visited, Graph)



for col in range(N):
    Graph[col] = list(map(int, sys.stdin.readline().split()))

while True:
    flag = 0
    DFS(0,0,visited,Graph)
    for i in range(N):
        for j in range(M):
            visited[i][j] = 0

    for i in range(N):
        for j in range(M):
            DFS(0,0,visited,Graph)

    for i in range(N):
        for j in range(M):
            if visited[i][j] >=2 and Graph[i][j] == 1 :
                Graph[i][j] = 0
                flag = 1

    if flag == 0:
        break

    answer += 1


print(answer)

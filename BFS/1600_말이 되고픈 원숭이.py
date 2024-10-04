import sys
from collections import deque

def bfs(k, W, H, board):
    dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dy = [0, 0, -1, 1]
    hx = [2, 2, -2, -2, 1, 1, -1, -1]  # 말의 이동
    hy = [1, -1, 1, -1, 2, -2, 2, -2]

    queue = deque([(0, 0, k, 0)])  # (x, y, 남은 K, 현재 이동 횟수)
    visited = [[[False] * (k + 1) for _ in range(W)] for _ in range(H)]
    visited[0][0][k] = True

    while queue:
        x, y, remaining_k, count = queue.popleft()

        # 도착점에 도달한 경우
        if x == H - 1 and y == W - 1:
            return count

        # 인접한 칸으로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0 and not visited[nx][ny][remaining_k]:
                visited[nx][ny][remaining_k] = True
                queue.append((nx, ny, remaining_k, count + 1))

        # 말의 이동으로 이동
        if remaining_k > 0:
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]
                if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0 and not visited[nx][ny][remaining_k - 1]:
                    visited[nx][ny][remaining_k - 1] = True
                    queue.append((nx, ny, remaining_k - 1, count + 1))

    return -1  # 도착할 수 없는 경우

# 입력 받기
k = int(input())
W, H = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
# 결과 출력
print(bfs(k, W, H, board))

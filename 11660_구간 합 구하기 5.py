import sys

N, K = map(int,sys.stdin.readline().split())
arr = [[0 for row in range(N)] for col in range(N)]

for i in range(N):
    arr[i] = (list(map(int,sys.stdin.readline().split())))

for _ in range(K):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    answer = 0
    for i in range(x1-1,x2):
        for j in range(y1-1,y2):
            answer += arr[i][j]

    print(answer)
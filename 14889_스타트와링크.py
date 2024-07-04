import sys
N = int(input())
arr = [0] * N

for i in range(N):
    arr[i] = list(map(int,sys.stdin.readline().split()))

visited = [False] * N
result = sys.maxsize
def dfs(a, idx):
    global result

    if a == N//2:

        start = 0
        link = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]

        result = min(result,abs(start-link))
        return

    else:
        for i in range(idx,N):
            if not visited[i]:
                visited[i] = True
                dfs(a+1, i+1)
                visited[i] = False

dfs(0,0)
print (result)



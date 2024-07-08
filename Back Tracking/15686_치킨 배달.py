import sys

N, M = map(int, sys.stdin.readline().split())

home = []
chicken = []
answer = 987654321

for i in range(N):  # 집과 치킨의 좌표를 리스트에 넣어준다.
    row = list(map(int, input().split()))

    for j in range(N):
        if row[j] == 1:
            home.append((i, j))
        elif row[j] == 2:
            chicken.append((i, j))

visited = [False] * len(chicken)


def dfs(idx, cnt):
    global answer

    if cnt == M:
        ans = 0

        for i in home:  # 집 좌표에 대해 모든 치킨집과의 거리를 구함
            distance = 9999999  # 거리를 큰 수로 정의
            for j in range(len(visited)):
                if visited[j]:
                    check_num = abs(i[0] - chicken[j][0]) + abs(i[1] - chicken[j][1])
                    distance = min(distance, check_num)  # 각 집에 대해 치킨 거리가 최소인 값을 구함
            ans += distance
        answer = min(ans, answer)

        return

    for i in range(idx, len(chicken)):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, cnt + 1)
            visited[i] = False

dfs(0,0)

print(answer)
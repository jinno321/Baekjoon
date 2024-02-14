import sys

T = int(input())
for _ in range(T):
    answer = "NO"
    N, M, W = map(int, sys.stdin.readline().split())
    edges = [] #간선정보 저장 배열
    for i in range(M):
        start, end, weight = map(int, sys.stdin.readline().split())
        edges.append((start, end, weight))  # 가중 그래프 삽입
        edges.append((end,start,weight))
    for i in range(W):
        start, end, weight = map(int, sys.stdin.readline().split())
        edges.append((start, end, -weight))  # 음수 그래프 삽입

    dis = [int(1e9)] * (N + 1)  # 그래프 무한대로 초기화

    for i in range(N):
        for node in edges: #간선정보 저장된 배열에서
            start, end, weight = node #하나씩 뽑아서
            if dis[end] > dis[start] + weight: #갱신할수 있는지 확인
                dis[end] = dis[start] + weight #더 작으면 갱신
                if i == N-1: answer = "YES"

    print(answer)

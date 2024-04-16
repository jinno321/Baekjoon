import sys
sys.setrecursionlimit(100000000)
K = int(input())

def DFS(start,visited,graph,group):
    visited[start] = group

    for v in graph[start]:
        if visited[v]==0: #아직 방문하지 않은 노드
            result = DFS(v,visited,graph,-group)
            if not result:
                return False
        else:
            if visited[v] == group:
                return False
    return True

for _ in range(K):
    V , E = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for i in range(E):
        start,end = map(int,sys.stdin.readline().split())
        graph[start].append(end)
        graph[end].append(start)

    for i in range(1,V+1):
        if visited[i] == 0:
            result = DFS(i,visited,graph,1)
            if not result: break
    if result:
         print("YES")
    else: print("NO")

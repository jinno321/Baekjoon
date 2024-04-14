import sys
sys.setrecursionlimit(10**5)
N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N+1)]

# 특정 원소가 속한 집합을 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(M):
    x, a, b = map(int, sys.stdin.readline().split())
    if x == 0: union(a,b)
    else:
        if find(a) == find(b): print("YES")
        else: print("NO")
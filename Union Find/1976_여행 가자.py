import sys
answer = "YES"
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    fa = find(a)
    fb = find(b)

    if fa>fb:
        parents[fa] = parents[fb]
    else:
        parents[fb] = parents[fa]

N, M = int(input()), int(input())
parents = [i for i in range(N)]
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        if arr[j] == 1:
            union(i,j)

link = list(map(int,input().split()))
start = link[0] - 1
for i in range(1,len(link)):
    if find(start) != find(link[i]-1):
        answer = "NO"
        break
    start = link[i]-1

print(answer)

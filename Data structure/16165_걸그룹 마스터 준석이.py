import sys;

N,M = map(int,sys.stdin.readline().split())
arr = []

for _ in range(N):
    group_name = str(input())
    for i in range(int(input())):
        girl = str(input())
        arr.append((group_name,girl))
arr.sort()

for _ in range(M):
    name = str(input())
    quiz = int(input())
    if quiz == 1:
        for node in arr:
            if node[1] == name:
                print(node[0])
    elif quiz == 0:
        for node in arr:
            if node[0] == name:
                print(node[1])




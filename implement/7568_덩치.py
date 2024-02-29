import sys

N = int(input())
arr = []
answer = []

for _ in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    arr.append([weight,height])

for i in range(N):
    rank = 1
    weight, height = arr[i]
    for j in range(N):
        if weight < arr[j][0] and height < arr[j][1]:
            rank += 1
    print(rank, end=" ")


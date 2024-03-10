import sys

N, M = map(int, sys.stdin.readline().split())
arr1 = []
arr2 = []
answer = []

for _ in range(N):
    x = input()
    arr1.append(x)


for _ in range(M):
    name = input()
    arr2.append(name)
answer = list(set(arr1) & set(arr2))
answer.sort()
print(len(answer))
for name in answer:
    print(name)


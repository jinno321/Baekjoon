import sys

N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
answer = [-1] * N
stack = []

stack.append(0)
for i in range(1, N):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

for i in answer:
    print(i,end=" ")


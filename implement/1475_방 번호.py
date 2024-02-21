import sys

N = int(input())

i = len(str(N))

arr = [0 for _ in range(10)]

for a in range(i-1, -1, -1):
    if N // (10 ** a) == 9:
        arr[6] += 1
    else:
        arr[N//(10**a)] +=1
    N = N % (10 ** a)
answer = 0
for i in range(10):
    if i == 6:
        if answer < arr[i] // 2 + arr[i] % 2:
            answer = arr[i] // 2 + arr[i] % 2
    else:
        if answer < arr[i]:
            answer = arr[i]
print(answer)

import sys

X, Y = list(map(int, sys.stdin.readline().split()))
Z = (Y*100 // X)
answer = -1
sub = X - Y


def binary_search(low, high):
    global answer
    mid = (low + high) // 2
    if (low == high):
        answer = low
        return
    if Z == (mid*100)//(mid+sub):
        binary_search(mid + 1, high)
    else:
        binary_search(low, mid)

binary_search(Y+1, 1000000000)
if Z == 99 or Z ==100:
    print(-1)
elif answer - Y <= 0:
    print(-1)
else:
    print(answer - Y)

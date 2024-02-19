import sys

A,B,C = map(int, sys.stdin.readline().split())
answer = 1

def dac(A,B,C):
    if B == 1:
        return A % C
    elif B % 2 == 0:
        return (dac(A,B//2,C) **2) % C
    else:
        return ((dac(A,B//2,C) **2)*A) % C

print(dac(A,B,C))


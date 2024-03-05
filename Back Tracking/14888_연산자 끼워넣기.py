import sys

N = int(input())
num = list(map(int, sys.stdin.readline().split()))
# + - * / 순으로 보유 개수 저장
plus, minus, multi, divide = map(int, sys.stdin.readline().split())
high = -1e9
low = 1e9


def dfs(count, result, plus, minus, multi, divide):
    global high, low
    if count == N:  # 종료조건
        high = max(high, result)
        low = min(low, result)
        return

    if plus > 0:
        dfs(count + 1, result + num[count], plus - 1, minus, multi, divide)
    if minus > 0:
        dfs(count + 1, result - num[count], plus, minus - 1, multi, divide)
    if multi > 0:
        dfs(count + 1, result * num[count], plus, minus, multi - 1, divide)
    if divide > 0:
        dfs(count + 1, int(result / num[count]), plus, minus, multi, divide - 1)


dfs(1, num[0],plus,minus,multi,divide)
print(int(high))
print(int(low))

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [float("inf")] * 100001
Queue = deque()
Queue.append(N)
visited[N] = 0


def find():
    global Queue
    global N, K
    while Queue:
        num = Queue.popleft()
        if num == K:
            count = 1
            while Queue:
                pop = Queue.popleft()
                if pop == K: count += 1
            return visited[num], count
        else:
            if num + 1 <= 100000 and visited[num] < visited[num + 1]:
                visited[num + 1] = visited[num] + 1
                Queue.append(num + 1)
            if 0 <= num - 1 <= 100000 and visited[num] < visited[num - 1]:
                visited[num - 1] = visited[num] + 1
                Queue.append(num - 1)
            if num * 2 <= 100000 and visited[num] < visited[num * 2]:
                visited[num * 2] = visited[num] + 1
                Queue.append(num * 2)
    return -1


time, way = find()
print(time)
print(way)

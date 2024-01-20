
import sys
from bisect import bisect_left

N = int(input())
count = 0

arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
for i in range(N):
    now = arr[i]
    low = i+1
    high = N-1
    while(low <high):
        if (arr[low]+arr[high] + now > 0):
            high-=1
        else:
            if arr[low] + arr[high] + now == 0:
                if(arr[low] == arr[high]):
                    count+=high-low
                else:
                    K=bisect_left(arr,arr[high])
                    count+=high-K+1
            low+=1    

print(count)

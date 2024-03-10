N = int(input())
count5 = 0
answer = -1
while count5 * 5 <= N:
    if (N - count5 * 5)% 3 == 0:
        answer = ((N - count5 * 5) // 3) + count5
    count5+=1

print(answer)


import sys
Dice = []

N = int(input())
Dice = list(map(int,sys.stdin.readline().split()))
answer = 0
#중간에 1개 나오는거는 그냥 최솟값 때려박아
#2개 노출되는 면이 가능한거
Twomin = float('inf')
Threemin = float('inf')

for i in range(6):
    for j in range(6):
        if i == j: continue
        if i+j == 5: continue
        Twomin = min(Twomin,Dice[i]+Dice[j])

Threemin = min(Dice[0]+Dice[1]+Dice[2],Dice[0]+Dice[1]+Dice[3],Dice[0]+Dice[3]+Dice[4],Dice[0]+Dice[2]+Dice[4])
Threemin = min(Threemin,Dice[5]+Dice[1]+Dice[2],Dice[5]+Dice[1]+Dice[3],Dice[5]+Dice[3]+Dice[4],Dice[5]+Dice[2]+Dice[4])

if N==1:
    answer += sum(Dice) - max(Dice)
if N>=2:
    #디폴트값
    answer += Threemin * 4
    answer += Twomin * 4

if N > 2:
    answer += min(Dice) * (N-2) * (N-2) * 5 #1면만 노출되는거
    answer += min(Dice) * (N-2) * 4 # 밑 바닥 붙어있는 1면 보이는거
    answer += Twomin * (N-2) * 8 # 옆 모서리

print(answer)
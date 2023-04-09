'''
1. 정육면체 숫자 변화
    - 칸에 쓰여진 수가 0이면, 주사위 바닥면 숫자가 칸으로 복사된다.
    - 칸에 쓰여진 수가 != 0, 칸에 쓰여진 수가 정육면체 바닥으로 복사, 해당 칸은 0이됨
    - 정육면체는 격자 밖으로 이동 못함. 이동하려고 하면 무시하고 출력도 X
'''

dR = [0, 0, -1, 1]
dC = [1, -1, 0, 0]

n, m, r, c, k, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
movements = list(map(int, input().split()))

def moveDice(dice, movement):
    if movement == 0:
        newDice = [dice[4], dice[1], dice[0], dice[3], dice[5], dice[2]]
    elif movement == 1:
        newDice = [dice[2], dice[1], dice[5], dice[3], dice[0], dice[4]]
    elif movement == 2:
        newDice = [dice[1], dice[5], dice[2], dice[0], dice[4], dice[3]]
    else:
        newDice = [dice[3], dice[0], dice[2], dice[5], dice[4], dice[1]]
    return newDice

# if arr[r][c] == 0:
dice = [0, 0, 0, 0, 0, 0]
# else:
#     dice = [0, 0, 0, 0, 0, arr[r][c]]
# print(dice[0])
for movement in movements:
    movedR, movedC, = r + dR[movement - 1], c + dC[movement - 1]
    if not 0 <= movedR < n or not 0 <= movedC < m:
        continue
    r, c = movedR, movedC
    dice = moveDice(dice, movement - 1)
    if arr[r][c] == 0:
        arr[r][c] = dice[-1]
    else:
        dice[-1] = arr[r][c]
        arr[r][c] = 0
    print(dice[0])


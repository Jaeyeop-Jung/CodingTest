# TODO 틀림 잘 생각해봐 맞을 수 있다

import sys

input = sys.stdin.readline

n, m, r, c, k, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]

# 상 동 하 서 = 서 상 동 하

def turn(move):
    if move == 1:
        dice[0], dice[1], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[1]
    elif move == 2:
        dice[0], dice[1], dice[3], dice[5] = dice[1], dice[5], dice[0], dice[3]
    elif move == 3:
        dice[0], dice[2], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[2]
    else:
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[5], dice[0], dice[4]


dR = [0, 0, -1, 1]
dC = [1, -1, 0, 0]

for command in commands:
    movedR, movedC = r + dR[command - 1], c + dC[command - 1]
    if not 0 <= movedR < n or not 0 <= movedC < m:
        continue
    turn(command)
    if arr[movedR][movedC] == 0:
        arr[movedR][movedC] = dice[-1]
    else:
        dice[-1] = arr[movedR][movedC]
        arr[movedR][movedC] = 0
    print(dice[0])
    r, c = movedR, movedC


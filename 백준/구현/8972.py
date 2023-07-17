import math
import sys
from collections import defaultdict

input = sys.stdin.readline

dR = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dC = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

n, m, = map(int, input().split())
arr = []
enemy = []
for r in range(n):
    temp = list(input().strip())
    for c in range(m):
        if temp[c] == 'I':
            jongsu = [r, c]
        elif temp[c] == 'R':
            enemy.append((r, c))
    arr.append(temp)
moves = list(map(int, list(input().strip())))

def moveJongsu():
    global jongsu
    d = moves[i] - 1
    r, c, = jongsu
    arr[r][c] = '.'
    movedR, movedC = r + dR[d], c + dC[d]
    if arr[movedR][movedC] == 'R':
        return True
    arr[movedR][movedC] = 'I'
    jongsu = [movedR, movedC]
    return False

def moveEnemy():
    global enemy
    jR, jC = jongsu
    newEnemy = defaultdict(int)
    for eR, eC in enemy:
        next = (eR, eC)
        cost = math.inf
        for d in range(len(dR)):
            movedR, movedC = eR + dR[d], eC + dC[d]
            if not 0 <= movedR < n or not 0 <= movedC < m:
                continue
            if abs(jR - movedR) + abs(jC - movedC) < cost:
                next = (movedR, movedC)
                cost = abs(jR - movedR) + abs(jC - movedC)
        newEnemy[next] += 1

        # 4
        movedR, movedC = next
        if arr[movedR][movedC] == 'I':
            return True

        arr[eR][eC] = '.'
        arr[movedR][movedC] = 'R'

    # 5
    for key in newEnemy:
        if 2 <= newEnemy[key]:
            r, c, = key
            arr[r][c] = '.'
            newEnemy[key] = 0

    enemy = [key for key in newEnemy if 1 <= newEnemy[key]]
    return False


for i in range(len(moves)):
    # 1. 종수 이동, 2. 부딪혔는가
    if moveJongsu():
        print(f'kraj {i + 1}')
        exit()

    # 3. 아두이노 이동, 4. 종수가 있는가, 5. 2개 이상 아두이노 폭발
    if moveEnemy():
        print(f'kraj {i + 1}')
        exit()

for i in arr:
    for j in i:
        print(j, end='')
    print()
# 1. 사람의 순서대로 본인의 방향대로 한칸 이동
#   만약 범위 밖이면 정반대 방향으로 바꾸어 1만큼 이동
# 2-1. 이동한 방향에 플레이어가 없다면 해당 칸에 총이 있는지 확인
#       가진 총과 맵의 총 중 가장 강력한 총을 흭득하고 나머지는 맵에 둠
# 2-2. 플레이어가 있다면 [플레이어의 초기 능력치 + 총의 공격력합, 플레이어의 초기 능력치]로 경기를함
#       이긴 플레이어는 능력치의 합의 차 만큼 포인트를 얻음
# 2-2-1. 진 플레이어는 본인의 총을 격자에 놓고, 해당 플레이어가 가던 방향으로 이동
#       만약 방향에 다른 플레이어나, 격자 범위 밖이면 시게 90도씩 회전하며 빈칸이 보이면 이동.
#       해당 칸에 총이 있으면 총을 흭득
# 2-2-2. 이긴 플레이어 총 흭득

dR = [-1, 0, 1, 0]
dC = [0, 1, 0, -1]

n, m, k = map(int, input().split())
arr = [[[] for _ in range(n)] for _ in range(n)]
for r in range(n):
    temp = list(map(int, input().split()))
    for c in range(n):
        if temp[c] != 0:
            arr[r][c].append(temp[c])
player = []
playerArr = [[[] for _ in range(n)] for _ in range(n)]
for num in range(m):
    r, c, d, s = map(int, input().split())
    player.append([r - 1, c - 1, d, s, 0, 0])
    playerArr[r - 1][c - 1].append(num)

def getWinner(num1, s1, g1, num2, s2, g2):
    if s2 + g2 < s1 + g1:
        return num1, num2
    elif s1 + g1 < s2 + g2:
        return num2, num1
    else:
        if s2 < s1:
            return num1, num2
        else:
            return num2, num1

for _ in range(k):
    for num in range(m):
        # 1
        r, c, d, s, score, gun = player[num]
        movedR, movedC = r + dR[d], c + dC[d]
        if not 0 <= movedR < n or not 0 <= movedC < n:
            d = (d + 2) % 4
            movedR, movedC = r + dR[d], c + dC[d]
        player[num] = [movedR, movedC, d, s, score, gun]
        playerArr[r][c].remove(num)
        playerArr[movedR][movedC].append(num)

        # 2-1
        if len(playerArr[movedR][movedC]) == 1:
            if arr[movedR][movedC]:
                maxGun = max(arr[movedR][movedC])
                if gun < maxGun:
                    if gun != 0:
                        arr[movedR][movedC].append(gun)
                    gun = maxGun
                    arr[movedR][movedC].remove(maxGun)
                player[num] = [movedR, movedC, d, s, score, gun]

        # 2-2
        else:
            # 2-2-1
            rivalNum = playerArr[movedR][movedC][0]
            _, _, rivalD, rivalS, rivalScore, rivalGun, = player[rivalNum]
            winner, loser, = getWinner(num, s, gun, rivalNum, rivalS, rivalGun)
            player[winner][4] += abs(rivalS + rivalGun - s - gun)

            # 2-2-2
            if player[loser][-1] != 0:
                arr[movedR][movedC].append(player[loser][-1])
                player[loser][-1] = 0
            loserD = player[loser][2]
            for i in range(4):
                loserMovedR, loserMovedC = movedR + dR[(loserD + i) % 4], movedC + dC[(loserD + i) % 4]
                if not 0 <= loserMovedR < n or not 0 <= loserMovedC < n or playerArr[loserMovedR][loserMovedC]:
                    continue
                player[loser][0], player[loser][1], player[loser][2] = loserMovedR, loserMovedC, (loserD + i) % 4
                playerArr[loserMovedR][loserMovedC].append(loser)
                playerArr[movedR][movedC].remove(loser)
                if arr[loserMovedR][loserMovedC]:
                    maxGun = max(arr[loserMovedR][loserMovedC])
                    player[loser][-1] = maxGun
                    arr[loserMovedR][loserMovedC].remove(maxGun)
                break

            # 2-2-3
            if arr[movedR][movedC]:
                maxGun = max(arr[movedR][movedC])
                if player[winner][-1] < maxGun:
                    if player[winner][-1] != 0:
                        arr[movedR][movedC].append(player[winner][-1])
                    player[winner][-1] = maxGun
                    arr[movedR][movedC].remove(maxGun)


result = [i[-2] for i in player]
print(*result)
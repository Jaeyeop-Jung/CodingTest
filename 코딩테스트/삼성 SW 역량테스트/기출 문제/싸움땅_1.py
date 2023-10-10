
#   플레이
#   1. 1번 플레이어부터 순차적으로 바라보고 있는 방향으로 움직인다
#   2. 만약 격자 밖이면 정반대로 바꾸고 이동한다
#   3-1. 이동한 방향에 플레이어가 없으면 가장 쎈 총을 갖는다
#   4-1. 있으면, 초기 능력치 + 총의 공격력 합으로 싸우고 이도 같다면 초기 능력치가 높은 플레이어가 승리한다
#       승리한 플레이어는 초기 능력치 + 총의 공격력 합의 차 만큼 포인트를 얻는다
#   4-2. 진 플레이어는 총을 격자에 두고, 원래 방향으로 움직인다.
#        만약에 이미 플레이어가 있거나, 격자 밖이면 90도를 회전한다
#        해당 칸에 총이 있으면 줍는다
#   4-3 이긴 플레이어는 총들 중 가장 강한 총을 줍는다

dR = [-1, 0, 1, 0]
dC = [0, 1, 0, -1]

n, m, k, = map(int, input().split())
gun = [[[] for _ in range(n)] for _ in range(n)]
for r in range(n):
    temp = list(map(int, input().split()))
    for c in range(n):
        if 0 < temp[c]:
            gun[r][c].append(temp[c])
arr = [[[] for _ in range(n)] for _ in range(n)]
people = {}
for num in range(m):
    r, c, d, initAttack = map(int, input().split())
    people[num] = [r - 1, c - 1, d, initAttack, 0]
    arr[r - 1][c - 1].append(num)

def inRange(r, c):
    if not 0 <= r < n or not 0 <= c < n:
        return False
    return True

def move(num):
    r, c, d, initAttack, gunAttack, = people[num]
    movedR, movedC = r + dR[d], c + dC[d]
    if not inRange(movedR, movedC):
        d = (d + 2) % 4
        movedR, movedC = r + dR[d], c + dC[d]
    people[num] = [movedR, movedC, d, initAttack, gunAttack]
    arr[r][c].remove(num)
    arr[movedR][movedC].append(num)

def pickGun(num):
    r, c, d, initAttack, gunAttack, = people[num]
    if gunAttack != 0:
        gun[r][c].append(gunAttack)
    if not gun[r][c]:
        return
    maxGun = max(gun[r][c])
    people[num] = r, c, d, initAttack, maxGun
    gun[r][c].remove(maxGun)

def fight(num):
    r, c, _, _, _ = people[num]
    score = []
    for fightMemberNum in arr[r][c]:
        _, _, _, initAttack, gunAttack, = people[fightMemberNum]
        score.append([fightMemberNum, initAttack, gunAttack])
    score.sort(key=lambda x: (-(x[1] + x[2]), -x[1]))
    winner, winnerInitAttack, winnerGunAttack = score[0]
    loser, loserInitAttack, loserGunAttack = score[1]
    res[winner] += winnerInitAttack + winnerGunAttack - (loserInitAttack + loserGunAttack)
    return winner, loser

def loserAction(num):
    r, c, d, initAttack, gunAttack, = people[num]
    if gunAttack != 0:
        gun[r][c].append(gunAttack)
    people[num] = [r, c, d, initAttack, 0]

    for i in range(4):
        nD = (d + i) % 4
        movedR, movedC = r + dR[nD], c + dC[nD]
        if not inRange(movedR, movedC) or arr[movedR][movedC]:
            continue
        arr[r][c].remove(num)
        people[num] = [movedR, movedC, nD, initAttack, 0]
        arr[movedR][movedC].append(num)
        pickGun(num)
        break


res = [0] * m
for _ in range(k):
    for num in people:
        # 이동
        move(num)

        r, c, _, _, _ = people[num]
        # 플레이어가 없으면
        if len(arr[r][c]) == 1:
            pickGun(num)

        # 플레이어가 있으면
        else:
            winner, loser, = fight(num)
            loserAction(loser)
            pickGun(winner)

print(*res)
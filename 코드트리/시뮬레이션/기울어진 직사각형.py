n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dR = [-1, -1, 1, 1]
dC = [1, -1, -1, 1]

comb = [(i, j) for i in range(1, 21) for j in range(1, 21)]


def inRange(r, c):
    if not 0 <= r < n or not 0 <= c < n:
        return False
    return True


result = 0
for r in range(n):
    for c in range(n):
        for fst, sec in comb:
            temp = 0
            curR, curC = r, c
            movement = [fst, sec, fst, sec]
            flag = False
            for d in range(4):
                for _ in range(movement[d]):
                    movedR, movedC = curR + dR[d], curC + dC[d]
                    if inRange(movedR, movedC):
                        temp += arr[movedR][movedC]
                        curR, curC = movedR, movedC
                    else:
                        flag = True
                        break
                if flag:
                    break
            else:
                result = max(result, temp)

print(result)

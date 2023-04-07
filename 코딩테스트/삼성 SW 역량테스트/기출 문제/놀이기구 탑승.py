
dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]
EMPTY = -1

n = int(input())
priority = [list(map(int, input().split())) for _ in range(n ** 2)]
ppriority = {i[0]: [i[1], i[2], i[3], i[4]] for i in priority}
arr = [[EMPTY] * n for _ in range(n)]
for idx in range(n ** 2):
    num, p1, p2, p3, p4 = priority[idx]
    tR, tC = n, n
    emptyCnt = 0
    priorityCnt = 0
    for r in range(n - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            if arr[r][c] != EMPTY:
                continue
            tempEmptyCnt = 0
            tempPriorityCnt = 0
            for i in range(4):
                movedR, movedC = r + dR[i], c + dC[i]
                if not 0 <= movedR < n or not 0 <= movedC < n:
                    continue
                if arr[movedR][movedC] == EMPTY:
                    tempEmptyCnt += 1
                elif arr[movedR][movedC] in [p1, p2, p3, p4]:
                    tempPriorityCnt += 1

            if priorityCnt < tempPriorityCnt:
                tR, tC = r, c
                priorityCnt = tempPriorityCnt
                emptyCnt = tempEmptyCnt
            elif priorityCnt == tempPriorityCnt and emptyCnt < tempEmptyCnt:
                tR, tC = r, c
                priorityCnt = tempPriorityCnt
                emptyCnt = tempEmptyCnt
            elif priorityCnt == tempPriorityCnt and emptyCnt == tempEmptyCnt:
                tR, tC = r, c
    arr[tR][tC] = num

result = 0
for r in range(n):
    for c in range(n):
        cnt = 0
        for i in range(4):
            movedR, movedC = r + dR[i], c + dC[i]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                continue
            if arr[movedR][movedC] in ppriority[arr[r][c]]:
                cnt += 1
        if cnt == 1:
            result += 1
        elif cnt == 2:
            result += 10
        elif cnt == 3:
            result += 100
        elif cnt == 4:
            result += 1000

print(result)
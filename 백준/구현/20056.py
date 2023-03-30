
dR = [-1, -1, 0, 1, 1, 1, 0, -1]
dC = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
fireBalls = {}
board = [[[] for _ in range(n)] for _ in range(n)]
ballCnt = m
for ballNum in range(m):
    r, c, m, s, d = map(int, input().split())
    fireBalls[ballNum] = [r - 1, c - 1, m, s, d]
    board[r - 1][c - 1].append(ballNum)

for _ in range(k):
    # 움직이기
    for ballNum in fireBalls:
        r, c, m, s, d, = fireBalls[ballNum]
        movedR, movedC = (r + dR[d] * s) % n, (c + dC[d] * s) % n
        fireBalls[ballNum] = [movedR, movedC, m, s, d]
        board[r][c].remove(ballNum)
        board[movedR][movedC].append(ballNum)

    # 2번 행동
    for r in range(n):
        for c in range(n):
            if 2 <= len(board[r][c]):
                # 질량 속력 총합
                length = len(board[r][c])
                totalM, totalS = 0, 0
                directions = []
                while board[r][c]:
                    ballNum = board[r][c].pop()
                    ballR, ballC, m, s, d, = fireBalls[ballNum]
                    totalM += m
                    totalS += s
                    directions.append(d % 2)
                    del fireBalls[ballNum]

                # 질량 속력 나누기
                eachM = int(totalM / 5)
                if eachM == 0:
                    continue
                eachS = int(totalS / length)
                if len(set(directions)) == 1:
                    eachD = [0, 2, 4, 6]
                else:
                    eachD = [1, 3, 5, 7]
                for d in eachD:
                    fireBalls[ballCnt] = [r, c, eachM, eachS, d]
                    board[r][c].append(ballCnt)
                    ballCnt += 1

result = 0
for ballNum in fireBalls:
    result += fireBalls[ballNum][2]
print(result)

import sys
input = sys.stdin.readline

WHITE = 0
RED = 1
BLUE = 2
dRow = [0, 0, 0, -1, 1]
dColumn = [0, 1, -1, 0, 0]

def getReverseDirection(d):
    if d % 2 == 0:
        return d - 1
    else:
        return d + 1

n, k, = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
pawn = []
for i in range(k):
    r, c, d = map(int, input().split())
    pawn.append([r - 1, c - 1, d])

# 각 칸의 말 순서를 나타내기 위한 리스트
status = [[[] for _ in range(n)] for _ in range(n)]
for i in range(len(pawn)):
    r, c, d = pawn[i]
    status[r][c].append(i)

# 턴마다
for turn in range(1, 1001):
    # k개의 말들을 이동시킨다
    for idx, v, in enumerate(pawn):
        r, c, d, = v

        # 맨 아래가 아니면 스킵
        if status[r][c].index(idx) != 0:
            continue

        movedR, movedC = r + dRow[d], c + dColumn[d]
        # 파란색일 때
        if (not 0 <= movedR < n or not 0 <= movedC < n) or board[movedR][movedC] == BLUE:
            d = getReverseDirection(d)
            movedR, movedC = r + dRow[d], c + dColumn[d]
            if (not 0 <= movedR < n or not 0 <= movedC < n) or board[movedR][movedC] == BLUE:
                pawn[idx][2] = d
                continue
            elif board[movedR][movedC] == RED:
                pawn[idx][2] = d
                status[movedR][movedC] += list(reversed(status[r][c][:]))
            elif board[movedR][movedC] == WHITE:
                pawn[idx][2] = d
                status[movedR][movedC] += status[r][c][:]
        # 흰색일 때
        elif board[movedR][movedC] == WHITE:
            status[movedR][movedC] += status[r][c][:]
        # 빨간색일 때
        elif board[movedR][movedC] == RED:
            status[movedR][movedC] += list(reversed(status[r][c][:]))

        # 이동한 말 위치 변경
        for movePawnIdx in status[movedR][movedC]:
            pawn[movePawnIdx][0], pawn[movePawnIdx][1] = movedR, movedC

        # 이동하기 전 장소 리스트 비우기
        status[r][c] = []

        # 게임이 끝났는지 판단
        if 4 <= len(status[movedR][movedC]):
            print(turn)
            exit()
print(-1)

# TODO 틀림 구현 실패

def solution(n, build_frame):
    board = [[[] * n for j in range(n)] for i in range(n)]
    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            if a == 0: # 기둥
                if y == 0 or 0 in board[x][y - 1] or 1 in board[x - 1][y] or 1 in board[x][y]:
                    board[x][y].append(a)
            if a == 1: # 보
                if x == 0:
                    if (1 in board[x][y] or 0 in board[x][y - 1]) and \
                        (0 in board[x + 1][y] or 1 in board[x + 1][y] or 0 in board[x + 1][y - 1]):
                        board[x][y].append(1)
                # else:
                    # if (1 in board[x - 1][y] or 0 in board[x][y - 1] or )

        # else:   # 제거


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
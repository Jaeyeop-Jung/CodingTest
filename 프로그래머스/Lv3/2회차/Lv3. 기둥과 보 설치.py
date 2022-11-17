# TODO 틀림

def make(board, r, c, kind):
    if kind == 0:   # 기둥
        if r == 0:  # 바닥 일때
            board[r][c].append(0)
            return True
        elif 0 <= c - 1 and 1 in board[r][c-1]:
            board[r][c].append(0)
            return True
        elif 0 in board[r-1][c]:
            board[r][c].append(0)
            return True
        return False
    else:
        if 0 in board[r-1][c] or 0 in board[r-1][c+1]:
            board[r][c].append(1)
            return True
        elif 1 in board[r][c-1] and 1 in board[r][c+1]:
            board[r][c].append(1)
            return True
        return False

def delete(board, r, c, kind):
    if kind == 0:   # 기둥
        if 0 in board[r+1][c]:
            return False
        elif 0 <= c - 1 and 1 in board[r + 1][c-1] and 0 not in board[r][c-1]:
            return False
        elif c + 1 <= len(board) and 1 in board[r+1][c] and 0 not in board[r][c+1]:
            return False

    else:   # 보
        if 0 <= c - 1 and 1 in board[r][c-1] and 0 not in board[r-1][c-1]:
            return False
        elif 1 in board[r][c+1] and 0 not in board[r-1][c+1]:
            return False
    board[r][c].remove(kind)
    return True

def solution(n, build_frame):
    result = []
    board = [[[] * (n + 1) for j in range(n + 1)] for i in range(n + 1)]
    for c, r, a, b in build_frame:
        temp = False
        if b == 1:
            temp = make(board, r, c, a)
            if temp:
                result.append([c, r, a])
        else:
            temp = delete(board, r, c, a)
            if temp:
                result.remove([c, r, a])
    result.sort(key=lambda x: (x[0], x[1], x[2]))
    return result


# print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
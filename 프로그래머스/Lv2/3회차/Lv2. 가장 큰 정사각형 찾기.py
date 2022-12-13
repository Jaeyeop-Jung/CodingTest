import math

dRow = [0, -1, -1]
dColumn = [-1, -1, 0]

def solution(board):
    result = [[0] * len(board[0]) for _ in range(len(board))]
    for r in range(len(result)):
        for c in range(len(result[r])):
            if board[r][c] != 1:
                continue
            minTemp = math.inf
            for i in range(3):
                movedR = r + dRow[i]
                movedC = c + dColumn[i]
                if not 0 <= movedR < len(board) or not 0 <= movedC < len(board[movedR]):
                    break
                minTemp = min(minTemp, result[movedR][movedC])
            else:
                result[r][c] = minTemp + 1
                continue
            result[r][c] = 1

    return max(map(max, result)) ** 2


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))
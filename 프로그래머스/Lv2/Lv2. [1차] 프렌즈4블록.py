from pprint import pprint
from collections import deque

dRow = [0, 0, 1, 1]
dColumn = [0, 1, 1, 0]

def removeBlock(m, n, board):
    removedBoard = [i[:] for i in board]
    removeCoord = []
    for row in range(len(board)):
        for column in range(len(board[row])):
            same = True
            for i in range(len(dRow)):
                movedRow = row + dRow[i]
                movedColumn = column + dColumn[i]
                if not 0 <= movedRow < m or not 0 <= movedColumn < n:
                    same = False
                    break
                if not board[row][column] == board[movedRow][movedColumn]:
                    same = False
                    break
            if same is True:
                for i in range(len(dRow)):
                    movedRow = row + dRow[i]
                    movedColumn = column + dColumn[i]
                    removeCoord.append([movedRow, movedColumn])
    for row, column in removeCoord:
        removedBoard[row][column] = ''
    return removedBoard

def downBlock(m, n, board):
    for column in range(n):
        queue = deque()
        emptyCount = 0
        for row in range(m - 1, -1, -1):
            if board[row][column] != '':
                queue.append(board[row][column])
            else:
                emptyCount += 1
        for i in range(m - 1, -1, -1):
            if queue:
                board[i][column] = queue.popleft()
            else:
                board[i][column] = ''

def solution(m, n, board):
    board = list(map(list, board))

    while True:
        tempBoard = removeBlock(m, n, board)
        if tempBoard[:][:] == board[:][:]:
            board = tempBoard
            break
        board = tempBoard[:][:]
        downBlock(m, n, board)

    return sum([i.count('') for i in board])

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
# TODO 틀림 https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A0%95%EC%82%AC%EA%B0%81%ED%98%95-%EC%B0%BE%EA%B8%B0-%EB%8F%99%EC%A0%81-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-dp

def solution(board):
    result = []
    dp = {}
    for startRow in range(len(board)):
        for startColumn in range(len(board[startRow])):
            if board[startRow][startColumn] == 0:
                continue
            same = True
            endRow, endColumn = startRow, startColumn
            for _ in range(len(board)):
                endRow, endColumn = endRow + 1, endColumn + 1
                if str(startRow) + str(startColumn) + str(endRow) + str(endColumn) in dp:
                    continue
                if not 0 <= endRow < len(board) or not 0 <= endColumn < len(board[startRow]):
                    result.append((endRow - startRow) * (endColumn - startColumn))
                    dp[str(startRow) + str(startColumn) + str(endRow) + str(endColumn)] = True
                    break
                for i in range(startRow, endRow + 1):
                    if board[i][endColumn] == 0:
                        same = False
                        break
                else:
                    for i in range(startColumn, endColumn + 1):
                        if board[endRow][i] == 0:
                            same = False
                            break
                if not same:
                    result.append((endRow - startRow) * (endColumn - startColumn))
                    dp[str(startRow) + str(startColumn) + str(endRow) + str(endColumn)] = True
                    break
    if not result:
        return 0
    return max(result)


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))
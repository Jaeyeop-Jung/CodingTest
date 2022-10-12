
direction = ['R', 'L', 'D', 'U']
dRow = [0, 0, 1, -1]
dColumn = [1, -1, 0, 0]

def solution(dirs):
    result = set()
    row, column = 0, 0
    for i in dirs:
        movedRow = row + dRow[direction.index(i)]
        movedColumn = column + dColumn[direction.index(i)]
        if not -5 <= movedRow <= 5 or not -5 <= movedColumn <= 5:
            continue
        result.add((row, column, movedRow, movedColumn))
        result.add((movedRow, movedColumn, row, column))
        row, column = movedRow, movedColumn
    return len(result) // 2

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
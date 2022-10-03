# TODO 틀림 https://velog.io/@tjdud0123/%EB%B0%A9%EB%AC%B8-%EA%B8%B8%EC%9D%B4

direction = ['U', 'R', 'D', 'L']
dRow = [-1, 0, 1, 0]
dColumn = [0, 1, 0, -1]

def solution(dirs):
    graph = [[[] for j in range(10)] for i in range(10)]
    row, column = 5, 5
    for i in range(len(dirs)):
        for j in range(len(direction)):
            if dirs[i] == direction[j]:
                movedRow = row + dRow[j]
                movedColumn = column + dColumn[j]
                if not 0 <= movedRow < 10 or not 0 <= movedColumn < 10:
                    break
                if dirs[i] in graph[movedRow][movedColumn] or direction[j - 2] in graph[row][column]:
                    break
                row, column = movedRow, movedColumn
        else:
            graph[row][column].append(dirs[i])
        if not 0 <= movedRow < 10 or not 0 <= movedColumn < 10:
            row, column = movedRow, movedColumn

    return sum([len(graph[i][j]) for i in range(10) for j in range(10) if graph[i][j]])


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
print(solution('UUUUUDDDDDDDDDD'))
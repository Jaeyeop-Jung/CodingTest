
dRow = [0, 0, 1, -1]
dColumn = [1, -1, 0, 0]
flag = False

def dfs(graph, cur, des, visited, routin):
    visited[cur[0]][cur[1]] = True
    if cur == des and routin.count('O') < 2 and len(routin) <= 2 and routin.count('X') < 1:
        global flag
        flag = True
        return
    elif cur == des:
        return
    for i in range(len(dRow)):
        movedRow = cur[0] + dRow[i]
        movedColumn = cur[1] + dColumn[i]
        if not 0 <= movedRow < 5 or not 0 <= movedColumn < 5:
            continue
        if abs(des[0] - movedRow) + abs(des[1] - movedColumn) > abs(des[0] - cur[0]) + abs(des[1] - cur[1]):
            continue
        if visited[movedRow][movedColumn] is False:
            routin.append(graph[movedRow][movedColumn])
            dfs(graph, [movedRow, movedColumn], des, visited, routin)
            visited[movedRow][movedColumn] = False
            routin.remove(graph[movedRow][movedColumn])

def solution(places):
    result = [1] * 5
    for i in range(len(places)):
        person = []
        for j in range(len(places[i])):
            for k in range(len(places[i][j])):
                if places[i][j][k] == 'P':
                    person.append([j, k])
        for j in range(len(person) - 1):
            for k in range(j + 1, len(person)):
                visited = [[False] * 5 for _ in range(5)]
                dfs(places[i], person[j], person[k], visited, [])
                global flag
                if flag is True:
                    result[i] = 0
                    flag = False
    return result

solution([
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
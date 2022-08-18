# TODO 틀림 https://ysyblog.tistory.com/161

dRow = [0, 0, 1, -1]
dColumn = [1, -1, 0, 0]
dRotate = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

result = 0

def dfs(graph, left, right, visited, cnt):
    visited[left[0]][left[1]] = True
    visited[right[0]][right[1]] = True
    for i in range(len(dRow)):
        movedLeft = [left[0] + dRow[i], left[1] + dColumn[i]]
        movedRight = [right[0] + dRow[i], right[1] + dColumn[i]]
        if movedLeft == [len(graph), len(graph)] or movedRight == [len(graph), len(graph)]:
            result = min(result, cnt + 1)
        if not 0 <= movedLeft[0] < len(graph) or not 0 <= movedLeft[1] < len(graph) or not 0 <= movedRight[0] < len(graph) or not 0 <= movedRight[1] < len(graph):
            continue
        if visited[movedLeft[0]][movedLeft[1]] is True and visited[movedRight[0]][movedRight[1]] is True:
            continue
        if graph[movedLeft[0]][movedLeft[1]] == 0 and graph[movedRight[0]][movedRight[1]] == 0:
            dfs(graph, movedLeft, movedRight, visited, cnt + 1)
            visited[movedLeft[0]][movedLeft[1]] = False
            visited[movedRight[0]][movedRight[1]] = False

    for i in range(len(dRotate)):
        if i % 2 == 0:
            oneStepMovedLeft = [left[0] + dRotate[i][0], left[1]]
            twoStepMovedLeft = [oneStepMovedLeft[0], oneStepMovedLeft[1] + dRotate[i][1]]
            if not 0 <= oneStepMovedLeft[0] < len(graph) or not 0 <= oneStepMovedLeft[1] < len(graph) or not 0 <= twoStepMovedLeft[0] < len(graph) or not 0 <= twoStepMovedLeft[1] < len(graph):
                continue
            if graph[oneStepMovedLeft[0]][oneStepMovedLeft[1]] == 1 or graph[twoStepMovedLeft[0]][twoStepMovedLeft[1]] == 1:
                continue
            dfs(graph, twoStepMovedLeft, right, visited, cnt + 1)
            visited[twoStepMovedLeft[0]][twoStepMovedLeft[1]] = False
            visited[right[0]][right[1]] = False
        else:
            oneStepMovedRight = [right[0] + dRotate[i][0], right[1]]
            twoStepMovedRight = [oneStepMovedRight[0], oneStepMovedRight[1] + dRotate[i][1]]
            if not 0 <= oneStepMovedRight[0] < len(graph) or not 0 <= oneStepMovedRight[1] < len(graph) or not 0 <= twoStepMovedRight[0] < len(graph) or not 0 <= twoStepMovedRight[1] < len(graph):
                continue
            if graph[oneStepMovedRight[0]][oneStepMovedRight[1]] == 1 or graph[twoStepMovedRight[0]][twoStepMovedRight[1]] == 1:
                continue
            dfs(graph, left, twoStepMovedRight, visited, cnt + 1)
            visited[left[0]][left[1]] = False
            visited[twoStepMovedRight[0]][twoStepMovedRight[1]] = False

def solution(board):
    visited = [[False] * len(board) for _ in range(len(board))]
    return dfs(board, [0, 0], [0, 1],visited, 0)

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))

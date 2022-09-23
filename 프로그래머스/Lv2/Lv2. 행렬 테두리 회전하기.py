from collections import deque

def solution(rows, columns, queries):
    arr = [[j for j in range((i - 1) * columns + 1, (i - 1) * columns + 1 + columns)] for i in range(1, rows + 1)]
    result = []
    queries = [[j - 1 for j in (queries[i])] for i in range(len(queries))]
    for startRow, startColumn, endRow, endColumn in queries:
        q = deque()
        # 회전할 값 넣기
        for i in range(endColumn - startColumn):
            q.append(arr[startRow][startColumn + i])
        for i in range(endRow - startRow):
            q.append(arr[startRow + i][endColumn])
        for i in range(endColumn - startColumn):
            q.append(arr[endRow][endColumn - i])
        for i in range(endRow - startRow):
            q.append(arr[endRow - i][startColumn])

        q.insert(0, q.pop())
        result.append(min(q))
        # 회전
        for i in range(endColumn - startColumn):
            arr[startRow][startColumn + i] = q.popleft()
        for i in range(endRow - startRow):
            arr[startRow + i][endColumn] = q.popleft()
        for i in range(endColumn - startColumn):
            arr[endRow][endColumn - i] = q.popleft()
        for i in range(endRow - startRow):
            arr[endRow - i][startColumn] = q.popleft()

    return result

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
# print(solution(100, 97, [[1,1,100,97]]))

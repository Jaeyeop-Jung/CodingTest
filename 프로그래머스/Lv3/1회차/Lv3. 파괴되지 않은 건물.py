# TODO 틀림

from pprint import pprint

def solution(board, skill):
    n = len(board)
    m = len(board[0])
    p = [[0 for i in range(m)] for j in range(n)]
    for t, r1, c1, r2, c2, d in skill:
        if t == 1:
            d *= -1

        p[r1][c1] += d
        if r2 + 1 < n:
            p[r2 + 1][c1] -= d
        if c2 + 1 < m:
            p[r1][c2 + 1] -= d
        if r2 + 1 < n and c2 + 1 < m:
            p[r2 + 1][c2 + 1] += d

    for r in range(n):
        for c in range(m - 1):
            p[r][c+1] += p[r][c]
    for c in range(m):
        for r in range(n - 1):
            p[r+1][c] += p[r][c]
    pprint(p)



print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
# print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))
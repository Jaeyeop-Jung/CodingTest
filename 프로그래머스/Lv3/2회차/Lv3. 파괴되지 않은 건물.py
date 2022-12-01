# TODO 틀림 그래도 1회차랑은 다르게 이해는 했으니까 낙담 ㄴㄴ

def solution(board, skill):
    total = [[0] * len(board[i]) for i in range(len(board))]
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree = -degree
        total[r1][c1] += degree
        if c2 + 1 < len(total[r1]):
            total[r1][c2 + 1] -= degree
        if r2 + 1 < len(total):
            total[r2 + 1][c1] -= degree
        if r2 + 1 < len(total) and c2 + 1 < len(total[r2]):
            total[r2 + 1][c2 + 1] += degree

    for r in range(len(total)):
        temp = 0
        for c in range(len(total[r])):
            temp += total[r][c]
            total[r][c] = temp

    for c in range(len(total[0])):
        temp = 0
        for r in range(len(total)):
            temp += total[r][c]
            total[r][c] = temp

    result = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            board[r][c] += total[r][c]
            if 0 < board[r][c]:
                result += 1
    return result


# print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))

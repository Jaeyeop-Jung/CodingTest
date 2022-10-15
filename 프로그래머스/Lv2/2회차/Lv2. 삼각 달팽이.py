from pprint import pprint


def solution(n):
    result = [[] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            result[i].append(0)

    cnt = 0
    row, column = -1, 0
    idx = 1
    for i in range(n, 0, -1):
        for j in range(i):
            if cnt == 0:
                row += 1
            elif cnt == 1:
                column += 1
            else:
                row, column = row - 1, column - 1
            result[row][column] = idx
            idx += 1
        cnt += 1
        cnt %= 3

    # return [result[i][j] for i in range(len(result)) for j in range(len(result[i]))]
    return sum(result, [])

print(solution(4))
# print(solution(5))
# print(solution(6))

# TODO 틀림 https://moondol-ai.tistory.com/395

def solution(n):
    if n == 1:
        return [1]

    result = [[0] * n for i in range(n)]
    cnt = 1
    status = -1
    x, y = -1, 0
    for i in range(n, 0, -1):
        status += 1
        status %= 3

        if status == 0:
            for j in range(i):
                x += 1
                result[x][y] = cnt
                cnt += 1
        elif status == 1:
            for j in range(i):
                y += 1
                result[x][y] = cnt
                cnt += 1
        else:
            for j in range(i):
                x -= 1
                y -= 1
                result[x][y] = cnt
                cnt += 1
    return [result[i][j] for i in range(len(result)) for j in range(len(result[i])) if not result[i][j] == 0]

# print(solution(4))
print(solution(5))
# print(solution(6))
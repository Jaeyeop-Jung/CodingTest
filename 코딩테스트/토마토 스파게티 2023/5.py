
def solution(A, B, C, D, N, Chips):
    arr = [[0] * B for _ in range(A)]
    for chip in Chips:
        r, c = chip
        arr[r][c] += 1

    res = 0
    for startR in range(A):
        for startC in range(B):
            if arr[startR][startC] == 0:
                continue
            temp = 0
            for curR in range(startR, startR + C + 1):
                for curC in range(startC, startC + D + 1):
                    if A <= curR or B <= curC:
                        break
                    temp += arr[curR][curC]
            res = max(res, temp)

            temp = 0
            for curR in range(startR, startR + D + 1):
                for curC in range(startC, startC + C + 1):
                    if A <= curR or B <= curC:
                        break
                    temp += arr[curR][curC]
            res = max(res, temp)

    return res

# print(solution(10, 10, 3, 2, 7, [[2, 2], [2, 3], [2, 4], [6, 2], [6, 3], [6, 4], [3, 5]]))
print(solution(1000, 1000, 30, 30, 1, [[0, 0]]))
# TODO 틀림

import math

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def getSum(r, c, rSep, cSep):
    result = 0
    for i in range(r, r + rSep):
        for j in range(c, c + cSep):
            result += arr[i][j]
    return result

result = -math.inf
# 세로
for cs1 in range(m):
    for rs1 in range(n):
        for cs2 in range(cs1 + 1, m):
            for rs2 in range(n):
                for c1Sep in range(1, cs2 - cs1 + 1):
                    for c2Sep in range(1, m - cs2 + 1):
                        for rs1Sep in range(1, n - rs1 + 1):
                            for rs2Sep in range(1, n - rs2 + 1):
                                temp = getSum(rs1, cs1, rs1Sep, c1Sep) + getSum(rs2, cs2, rs2Sep, c2Sep)
                                result = max(result, temp)

# 가로
for rs1 in range(n):
    for cs1 in range(m):
        for rs2 in range(rs1 + 1, n):
            for cs2 in range(m):
                for r1Sep in range(1, rs2 - rs1 + 1):
                    for r2Sep in range(1, n - rs2 + 1):
                        for cs1Sep in range(1, m - cs1 + 1):
                            for cs2Sep in range(1, m - cs2 + 1):
                                temp = getSum(rs1, cs1, rs1Sep, c1Sep) + getSum(rs2, cs2, rs2Sep, c2Sep)
                                result = max(result, temp)


print(result)


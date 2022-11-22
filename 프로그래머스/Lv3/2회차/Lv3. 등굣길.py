

def solution(m, n, puddles):
    available = [[True] * m for _ in range(n)]
    for c, r in puddles:
        available[r-1][c-1] = False
    dp = [[0] * m for _ in range(n)]
    for r in range(n):
        if not available[r][0]:
            break
        dp[r][0] = 1
    for c in range(m):
        if not available[0][c]:
            break
        dp[0][c] = 1

    for r in range(1, n):
        for c in range(1, m):
            if not available[r][c]:
                continue
            dp[r][c] = (dp[r-1][c] + dp[r][c-1]) % 1000000007

    return dp[-1][-1]

# print(solution(4, 3, [[2, 2]]))
# print(solution(1, 2, [[1,1]]))
# print(solution(100, 100, []))
print(solution(4, 4, [[2,2],[2,3]]))

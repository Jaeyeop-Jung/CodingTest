import math
import heapq

def solution(alp, cop, problems):
    maxAlp = max([problem[0] for problem in problems])
    maxCop = max([problem[1] for problem in problems])
    dp = [[math.inf] * (maxCop + 1) for _ in range(maxAlp + 1)]
    if maxAlp <= alp and maxCop <= cop:
        return 0
    elif maxAlp <= alp:
        dp[maxAlp][cop] = 0
    elif maxCop <= cop:
        dp[alp][maxCop] = 0
    else:
        dp[alp][cop] = 0

    # for curAlp in range(alp, maxAlp + 1):
    #     for curCop in range(cop, maxCop + 1):
    #         dp[curAlp][curCop] = min(dp[curAlp][curCop], dp[curAlp - 1][curCop] + 1)
    #         dp[curAlp][curCop] = min(dp[curAlp][curCop], dp[curAlp][curCop - 1] + 1)
    #         for problem in problems:
    #             nAlp, nCop, addAlp, addCop, cost = problem
    #             if nAlp <= curAlp and nCop <= curCop:
    #                 dp[curAlp][curCop] = min(dp[curAlp][curCop], dp[curAlp - addAlp][curCop - addCop] + cost)

    h = []
    heapq.heappush(h, [0, alp, cop])
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])
    while h:
        cost, curAlp, curCop = heapq.heappop(h)
        for problem in problems:
            nAlp, nCop, addAlp, addCop, price, = problem
            if nAlp <= curAlp and nCop <= curCop:
                nextAlp = min(maxAlp, curAlp + addAlp)
                nextCop = min(maxCop, curCop + addCop)
                if cost + price < dp[nextAlp][nextCop]:
                    dp[nextAlp][nextCop] = cost + price
                    heapq.heappush(h, [cost + price, nextAlp, nextCop])

    return dp[-1][-1]

# print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))
# print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))
print(solution(0, 0, [[1, 0, 1, 1, 0]]))
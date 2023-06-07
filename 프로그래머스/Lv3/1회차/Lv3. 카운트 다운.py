import math

def isLower(before, after):
    bCnt, bSingle, bBool = before
    aCnt, aSingle, aBool = after
    if bCnt < aCnt:
        return False
    if bCnt == aCnt and aSingle + aBool < bSingle + bBool:
        return False
    return True

def solution(target):
    scores = [i for i in range(1, 21)]
    dp = [[math.inf, 0, 0] for _ in range(target + 1)]
    dp[0] = [0, 0, 0]
    for i in range(target):
        cnt, single, bool = dp[i]
        if i + 50 <= target and isLower(dp[i + 50], [cnt + 1, single, bool + 1]):
            dp[i + 50] = [cnt + 1, single, bool + 1]
        for score in scores:
            if i + score * 1 <= target and isLower(dp[i + score * 1], [cnt + 1, single + 1, bool]):
                dp[i + score * 1] = [cnt + 1, single + 1, bool]
            if i + score * 3 <= target and isLower(dp[i + score * 3], [cnt + 1, single, bool + 1]):
                dp[i + score * 3] = [cnt + 1, single, bool]
            if i + score * 2 <= target and isLower(dp[i + score * 2], [cnt + 1, single, bool]):
                dp[i + score * 2] = [cnt + 1, single, bool]

    return [dp[-1][0], dp[-1][1] + dp[-1][2]]


# print(solution(21))
print(solution(58))

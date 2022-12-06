# TODO 틀림 쉬운 문제다 잘 생각해봐 풀 수 있어

# import math
# from collections import deque
#
# def solution(strs, t):
#     target = {i: t[:i] for i in range(1, len(t) + 1)}
#     n = len(t)
#
#     q = deque()
#     q.append(['', 0])
#
#     result = math.inf
#     while q:
#         cur, cnt = q.popleft()
#         if cur == t:
#             result = min(result, cnt)
#         for i in strs:
#             if len(cur + i) in target and cur + i == target[len(cur + i)]:
#                 q.append([cur + i, cnt + 1])
#
#     if result == math.inf:
#         return -1
#     return result
import math


def solution(strs, t):
    if len(t) == 1:
        if t in strs:
            return 1
        else:
            return -1

    dp = [math.inf] * (len(t) + 1)
    dp[0] = 0
    for i in range(1, len(t) + 1):
        j = i - 5 if 0 < i - 5 else 0
        for k in range(j, i):
            if t[k:i] in strs:
                dp[i] = min(dp[i], dp[k] + 1)
    return dp[-1] if dp[-1] != math.inf else -1

# print(solution(["ba","na","n","a"], "banana"))
# print(solution(["app","ap","p","l","e","ple","pp"], "apple"))
# print(solution(["ba","an","nan","ban","n"], "banana"))
print(solution(["ba", 'b', 'a'], 'babb' * 5000))
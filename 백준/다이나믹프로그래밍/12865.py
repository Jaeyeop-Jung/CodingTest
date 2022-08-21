# TODO 틀림 https://codingmovie.tistory.com/48

# import sys
#
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
# arr = [[0, 0]]
# weight = []
# for i in range(n):
#     w, v = map(int, input().split())
#     arr.append([w, v])
#     weight.append(w)
#
# dp = [0] * max(n + 1, k + 1, max(weight))
# for w, v in arr:
#     dp[w] = v
#
# for i in range(min(weight), len(dp)):
#     if i % 2 == 0:
#         for j in range(i // 2):
#             dp[i] = max(dp[i], dp[i -j] + dp[j])
#     else:
#         for j in range(i // 2 + 1):
#             dp[i] = max(dp[i], dp[i -j] + dp[j])
# print(dp[k])

n, k = map(int, input().split())
arr = []
for i in range(n):
    w, v = map(int, input().split())
    arr.append([w, v])

dp = [0] * (k + 1)
for w, v in arr:
    for i in range(k, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)

print(dp[k])


# TODO 틀림 잘 생각해봐 맞을 수 있다

# import math
# import sys
# import copy
#
# input = sys.stdin.readline
#
# for _ in range(3):
#     n = int(input())
#     total = 0
#     arr = []
#     for _ in range(n):
#         coin, num = map(int, input().split())
#         arr.append([coin, num])
#         total += coin * num
#
#     if total % 2 == 1:
#         print(0)
#         continue
#
#     dp = [math.inf] * (total + 1)
#     dp[0] = 0
#     for i in range(n):
#         coin, num, = arr[i]
#         for c in range()
#         for j in range(1, num + 1):
#             dp[j * coin] = min(dp[j * coin], dp[j - 1] + 1)
#
#     # cur = set()
#     # cur.add(0)
#     # for i in range(n):
#     #     coin, num = arr[i]
#     #     newCur = copy.deepcopy(cur)
#     #     for key in cur:
#     #         for j in range(1, num + 1):
#     #             if key + coin * j
#     #             newCur.add(key + coin * j)
#     #     cur = newCur
#     #
#     # if total / 2 in cur:
#     #     print(1)
#     # else:
#     #     print(0)
#
#     # print(dp[total // 2])

import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    coins = []
    target = 0
    for _ in range(N):
        a, b = map(int, input().split())
        coins.append([a, b])
        target += a*b

    if target&1:
        print(0)
        continue

    coins.sort(key=lambda x: -x[0])
    dp = [1] + [0] * (target + 1)
    for i in range(1, coins[0][1] + 1):
        dp[i * coins[0][0]] = 1
    for i in range(1, N):
        for j in range(coins[i][0], target):
            if dp[j - coins[i][0]]:
                for k in range(coins[i][1] + 1):
                    if target < j + k * coins[i][0]:
                        break
                    dp[j + k * coins[i][0]] = 1

    print(dp[target // 2])
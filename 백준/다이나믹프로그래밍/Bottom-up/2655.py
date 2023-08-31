# TODO 틀림
#
# n = int(input())
# arr = [[i] + list(map(int, input().split())) for i in range(n)]
#
# arr.sort(key=lambda x: (-x[2], -x[0], -x[3]))
# dp = []
# for i in range(n):
#     dp.append([arr[i][2], [arr[i][0]]])
#
# for i in range(n):
#     idx, area, height, weight = arr[i]
#     for j in range(i):
#         if weight < arr[j][-1]:
#             if dp[i][0] <= dp[j][0]:
#                 dp[i][0] = dp[j][0] + height
#                 dp[i][1] = dp[j][1][:] + [idx]
#
# dp.sort(key=lambda x: -x[0])
# print(len(dp[0][1]))
# for i in range(len(dp[0][1]) - 1, -1, -1):
#     print(dp[0][1][i] + 1)

n = int(input())
arr = [[i] + list(map(int, input().split())) for i in range(n)]

arr.sort(key=lambda x: -x[1])
dp = []
for i in range(n):
    dp.append([arr[i][2], [arr[i][0]]])

for i in range(n):
    idx, area, height, weight = arr[i]
    for j in range(i):
        if weight < arr[j][-1]:
            if dp[i][0] <= dp[j][0]:
                dp[i][0] = dp[j][0] + height
                dp[i][1] = dp[j][1][:] + [idx]

dp.sort(key=lambda x: -x[0])
print(len(dp[0][1]))
for i in range(len(dp[0][1]) - 1, -1, -1):
    print(dp[0][1][i] + 1)
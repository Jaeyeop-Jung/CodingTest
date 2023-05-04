# TODO 틀림


# n = int(input())
# arr = list(map(int, input().split()))
# arr = [[i, arr[i]] for i in range(n)]
# m = int(input())
#
# arr.sort(key=lambda x: (x[1], x[0]))
# dp = [''] * (m + 1)
# for i, v in arr:
#     for cur in range(v, m + 1):
#         if dp[cur - v] == '' and dp[cur] == '':
#             dp[cur] = str(i)
#         elif dp[cur - v] == '':
#             dp[cur] = max(dp[cur], i)
#         elif dp[cur] == '':
#             dp[cur] = max(dp[cur - v], i)
#         else:
#             dp[cur] = max(dp[cur], int(str(i) + str(dp[cur - v])))
#
# print(dp[m])

INF = 5001
n = int(input())
room = list(map(int, input().split()))
m = int(input())
dp = [-INF for _ in range(m+1)]
for i in range(n-1, -1, -1):
    x = room[i]
    for j in range(x, m+1):
        dp[j] = max(dp[j-x] * 10 + i, i, dp[j])

print(dp[m])
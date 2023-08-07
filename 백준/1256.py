# TODO 틀림

n, m, k = map(int, input().split())

dp = [[0] * (m + 1) for _ in range(n + 1)]
for r in range(n + 1):
    dp[r][0] = 1
for c in range(m + 1):
    dp[0][c] = 1

for r in range(1, n + 1):
    for c in range(1, m + 1):
        dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

def find(a, z, cur):
    if a == 0 and z == 0:
        global cnt
        cnt += 1
        if cnt == k:
            print(cur)
            exit()
        return
    if 0 < a:
        find(a - 1, z, cur + 'a')
    if 0 < z:
        find(a, z - 1, cur + 'z')

cnt = 1
for a in range(1, n):
    for z in range(m - 1, -1, -1):
        if k <= cnt + dp[a][z]:
            find(a, z, 'a' * (n - a) + 'z' * (m - z))
        cnt += dp[a][z] - 1


# cnt = 0
# z = m - 1
# for a in range(n):
#     if k <= cnt + dp[a][z]:
#         for z in range(m - 2, -1, -1):
#             if k <= cnt + dp[a][z] - 1:
#                 find(a, z, 'a' * (n - a) + 'z')
#                 exit()
#             cnt += dp[a][z] - 1
#     cnt += dp[a][z]
#
# a = n - 1
# for z in range(m):
#     if k <= cnt + dp[a][z] - 1:
#         find(a, z, 'z' * (m - z) + 'a')
#         exit()
#     cnt += dp[a][z]
#
# if cnt == k:
#     print('z' * m + 'a' * n)
# else:
#     print(-1)

# if dp[-1][-1] < k:
#     print(-1)
#     exit()
#
#
# cnt = 0
# z = m
# # a가 맨 앞일 때
# for a in range(n):
#     if z == -1:
#         break
#     if k < cnt + dp[a][z]:
#         find(a, z, 'a' * a + 'z' * z)
#     cnt += dp[a][z]
#     z -= 1
#
# a = 1
# # z가 맨 앞일 때
# for z in range(m - 1, -1, -1):
#     if k < cnt + dp[a][z]:
#         find(a, z, 'a' * a + 'z' * z)
#     cnt += dp[a][z]
#     a += 1
#
# print('z' * m + 'a' * n)
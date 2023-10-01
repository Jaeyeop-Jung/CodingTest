# TODO 틀림 아예 접근 방법이 틀렸다

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

visited = [False] * n
res = 0
for _ in range(3):
    diff = []
    left = 0
    right = -1
    cnt = 0
    total = 0
    while cnt < m and right < n:
        right += 1
        if not visited[right]:
            cnt += 1
            total += arr[right]

    diff.append((total, left, right))
    while left <= right and left < n and right < n:
        # 빼고
        if not visited[left]:
            total -= arr[left]
            cnt -= 1
        left += 1

        # 새로 넣고
        while cnt < m and right + 1 < n:
            right += 1
            if not visited[right]:
                cnt += 1
                total += arr[right]

        if left <= right:
            diff.append((total, left, right))

    diff.sort(key=lambda x: x[0])
    score, left, right = diff.pop()
    res += score
    for i in range(left, right + 1):
        visited[i] = True

print(res)
# import random
#
#
# def sol1(n, arr, m):
#     import sys
#
#     input = sys.stdin.readline
#
#     visited = [False] * n
#     res = 0
#     for _ in range(3):
#         diff = []
#         left = 0
#         right = -1
#         cnt = 0
#         total = 0
#         while cnt < m and right < n:
#             right += 1
#             if not visited[right]:
#                 cnt += 1
#                 total += arr[right]
#
#         diff.append((total, left, right))
#         while left <= right and left < n and right < n:
#             # 빼고
#             if not visited[left]:
#                 total -= arr[left]
#                 cnt -= 1
#             left += 1
#
#             # 새로 넣고
#             while cnt < m and right + 1 < n:
#                 right += 1
#                 if not visited[right]:
#                     cnt += 1
#                     total += arr[right]
#
#             if left <= right:
#                 diff.append((total, left, right))
#
#         diff.sort(key=lambda x: x[0])
#         score, left, right = diff.pop()
#         res += score
#         for i in range(left, right + 1):
#             visited[i] = True
#
#     return res
#
# def sol2(N, train, limit):
#     import sys
#
#     input = sys.stdin.readline
#
#     # 구간합 계산
#     S = [0]
#     value = 0
#     for t in train:
#         value += t
#         S.append(value)
#
#     dp = [[0] * (N + 1) for _ in range(4)]
#
#     # 점화식을 이용해 최댓값 탐색
#     for n in range(1, 4):
#         for m in range(n * limit, N + 1):
#             # n = 1일 때 선택한 객차가 없으므로
#             # 전에 계산한 구간합과 현재 계산하는 구간합 중 최댓값을 계산해 갱신해준다.
#             if n == 1:
#                 dp[n][m] = max(dp[n][m - 1], S[m] - S[m - limit])
#
#             # 점화식
#             else:
#                 dp[n][m] = max(dp[n][m - 1], dp[n - 1][m - limit] + S[m] - S[m - limit])
#             # print_dp(dp)
#
#     return dp[3][N]
#
# while True:
#     n = random.randrange(6, 15)
#     arr = [random.randrange(6, 15) for _ in range(n)]
#     while True:
#         m = random.randrange(1, 15)
#         if 1 <= m <= n // 3:
#             break
#     res1 = sol1(n, arr, m)
#     res2 = sol2(n, arr, m)
#     if res1 != res2:
#         print(n)
#         print(arr)
#         print(m)
#         print(res1)
#         print(res2)
#         break

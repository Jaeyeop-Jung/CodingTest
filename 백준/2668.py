# TODO 틀림 잘 생각해봐라

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = [int(input()) for _ in range(n)]
#
# resultCnt = 0
# resultState = 0
# result = []
# for i in range(len(arr)):
#     if i + 1 == arr[i]:
#         resultCnt = 1
#         result = [arr[i]]
#
# def dfs(up, down, idx):
#     global resultCnt
#     global result
#     global resultState
#     if up == down:
#         if resultCnt < len(up):
#             resultCnt = len(up)
#             result = sorted(up)
#             resultState = len(up)
#         else:
#             if resultState < len(up):
#                 return
#
#     for i in range(idx, n):
#         dfs(sorted(up + [i + 1]), sorted(down + [arr[i]]), i + 1)
#
# dfs([], [], 0)
# print(resultCnt)
# for i in result:
#     print(i)

import sys

input = sys.stdin.readline

n = int(input())
link = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(1, n + 1):
    link[i].append(int(input()))

ans = set()


def dfs(v, stack):
    for i in link[v]:
        if visited[i]:
            while stack:  # 사이클에 해당하는 모든 정점을 답에 넣음
                a = stack.pop()
                ans.add(a)
                if i == a:
                    break
            return

        visited[i] = True
        dfs(i, stack + [i])
        visited[i] = False


for i in range(1, n + 1):
    dfs(i, [])
ans = sorted(list(ans))
print(len(ans), *ans, sep='\n')
# TODO 틀림

# import sys
#
# input = sys.stdin.readline
#
# def dfs(start, idx, aFlag, bFlag, visited):
#     if aFlag and bFlag:
#         global res
#         res = True
#         return
#
#     if len(target) <= idx:
#         return
#
#     if not aFlag and not bFlag:
#         for i in range(start, len(visited)):
#             if a[idx] == target[i]:
#                 visited[i] = True
#                 if idx + 1 == len(a):
#                     dfs(0, 0, True, bFlag, visited)
#                 else:
#                     dfs(i + 1, idx + 1, aFlag, bFlag, visited)
#                 visited[i] = False
#
#     if aFlag and not bFlag:
#         for i in range(start, len(visited)):
#             if visited[i]:
#                 continue
#             if b[idx] == target[i]:
#                 visited[i] = True
#                 if idx + 1 == len(b):
#                     dfs(0, 0, aFlag, True, visited)
#                 else:
#                     dfs(i + 1, idx + 1, aFlag, bFlag, visited)
#                 visited[i] = False
#
#
# t = int(input())
# for test_case in range(1, t + 1):
#     a, b, target = input().strip().split(' ')
#     res = False
#
#     dfs(0, 0, False, False, [False] * len(target))
#
#     print(f'Data set {test_case}: yes' if res else f'Data set {test_case}: no')

import sys

input = sys.stdin.readline

t = int(input())
for test_case in range(1, t + 1):
    a, b, target = input().strip().split()

    aList = []
    bList = []
    for i in range(len(target)):
        for j in range(len(aList)):
            each = aList[j]
            if len(each) < len(a) and a[len(each)] == target[i]:
                aList.append(each[:])
                each.append(i)
        if a[0] == target[i]:
            aList.append([i])

        for j in range(len(bList)):
            each = bList[j]
            if len(each) < len(b) and b[len(each)] == target[i]:
                bList.append(each[:])
                each.append(i)
        if b[0] == target[i]:
            bList.append([i])

    for i in range(len(aList) - 1, -1, -1):
        if len(aList[i]) != len(a):
            aList.pop(i)
        else:
            aList[i] = set(aList[i])
    for i in range(len(bList) - 1, -1, -1):
        if len(bList[i]) != len(b):
            bList.pop(i)
        else:
            bList[i] = set(bList[i])

    res = False
    for i in aList:
        for j in bList:
            if len(i & j) == 0:
                res = True

    print(f'Data set {test_case}: yes' if res else f'Data set {test_case}: no')

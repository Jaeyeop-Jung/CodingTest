# TODO 틀림

# import random
#
#
# def sol1(n, arr):
#     import sys
#     from collections import deque
#
#     input = sys.stdin.readline
#
#     # n = int(input())
#     arr = [[i] + arr[i] for i in range(n)]
#
#     arr.sort(key=lambda x: (x[1], x[2]))
#     arr = deque(arr)
#     q = deque()
#     res = 0
#     resArr = []
#     while arr:
#         if not q:
#             q.append(arr.popleft())
#         while arr and arr[0][1] <= q[0][-1]:
#             q.append(arr.popleft())
#
#         if res <= len(q):
#             res = len(q)
#             resArr = [i[0] + 1 for i in q]
#         q.popleft()
#
#     return res
#
# def sol2(n, arr):
#     v = []
#     input_data = []
#
#     for i in range(n):
#         a, b = arr[i]
#         v.append((a, True))
#         v.append((b, False))
#         input_data.append((a, b))
#
#     v.sort(key=lambda x: (x[0], not x[1]))
#
#     curr = 0
#     ans = 0
#     position = 0
#
#     for i in range(len(v)):
#         if v[i][1]:
#             curr += 1
#         else:
#             curr -= 1
#         if curr > ans:
#             ans = curr
#             position = v[i][0]
#
#     return ans
#     # for i in range(len(input_data)):
#     #     if input_data[i][0] <= position <= input_data[i][1]:
#     #         print(i + 1, end=" ")
#
# while True:
#     n = random.randrange(3, 5)
#     arr = []
#     for _ in range(n):
#         arr.append(sorted([random.randrange(1, 10), random.randrange(1, 10)]))
#     arr.sort()
#
#     s1 = sol1(n, arr)
#     s2 = sol2(n, arr)
#     if s1 != s2:
#         print(n)
#         print(arr)
#         print(s1)
#         print(s2)
#         break

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [[i] + list(map(int, input().split())) for i in range(n)]

arr.sort(key=lambda x: (x[1], x[2]))
arr = deque(arr)
q = deque()
idx = 0
res = 0
resArr = []
while arr:
    if not q:
        q.append(arr.popleft())
    while arr and arr[0][1] <= q[0][-1]:
        q.append(arr.popleft())

    temp = list(q)[:]
    temp.sort(key=lambda x: x[1])
    flag = False
    for i, start, end in temp:
        if end < temp[-1][1]:
            flag = True
            break

    if not flag and res <= len(q):
        res = len(q)
        resArr = [i[0] + 1 for i in q]
    q.popleft()

print(res)
print(*resArr)
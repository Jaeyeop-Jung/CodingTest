# TODO 틀림 자료구조 뭐 쓸지 알테니까 그거 공부

# import sys
# input = sys.stdin.readline
#
# n, m, k = map(int, input().split())
# arr = [int(input()) for _ in range(n)]
#
# sumArr = [arr[0]]
# for i in range(1, n):
#     sumArr.append(sumArr[i - 1] + arr[i])
# change = {}
#
# cmd = [list(map(int, input().split())) for _ in range(m + k)]
# for a, b, c in cmd:
#     if a == 1:
#         change[b - 1] = c
#     else:
#         if b == c:
#             if b - 1 in change:
#                 print(change[b - 1])
#             else:
#                 print(arr[b - 1])
#             continue
#         result = sumArr[c - 1] - sumArr[b - 2 if 2 <= b else b - 1]
#         for key in change:
#             if b - 1 <= key <= c - 1:
#                 result += change[key]
#                 result -= arr[key]
#         print(result)

def update(i, dif):
    while i <= n:
        tree[i] += dif
        i += (i & -i)

def prefix_sum(i):
    result = 0
    while 1 <= i:
        result += tree[i]
        i -= (i & -i)
    return result

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [0] * (n + 1)
tree = [0] * (n + 1)

for i in range(1, n + 1):
    x = int(input())
    arr[i] = x
    update(i, x)

cmd = [list(map(int, input().split())) for _ in range(m + k)]
for a, b, c in cmd:
    if a == 1:
        update(b, c - arr[b])
        arr[b] = c
    else:
        print(prefix_sum(c) - prefix_sum(b - 1))
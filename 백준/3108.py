# TODO 틀림 아이디어는 맞았는데 잘 생각해봐

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = []
# for _ in range(n):
#     temp = list(map(int, input().split()))
#     arr.append(temp)
#
#
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
# def isConnect(rect1, rect2):
#     x1, y1, nx1, ny1 = arr[rect1]
#     x2, y2, nx2, ny2 = arr[rect2]
#     if nx1 < x2 or nx2 < x1 or ny1 < y2 or ny2 < y1:
#         return False
#     elif (x1 < x2 < nx2 < nx1 and y1 < y2 < ny2 < ny1) or \
#         (x2 < x1 < nx1 < nx2 and y2 < y1 < ny1 < ny2):
#         return False
#     return True
#
# def union_parent(parent, x, y):
#     if isConnect(x, y):
#         a = find_parent(parent, x)
#         b = find_parent(parent, y)
#         if a < b:
#             parent[b] = a
#         else:
#             parent[a] = b
#
# parent = [i for i in range(n)]
# for i in range(n):
#     for j in range(n):
#         union_parent(parent, i, j)
#
# for i in range(n):
#     find_parent(parent, i)
#
# res = len(set(parent))
# for i in range(n):
#     x, y, nx, ny = arr[i]
#     if (y <= 0 <= ny and (x == 0 or nx == 0)) or ((y == 0 or ny == 0) and x <= 0 <= nx):
#         res -= 1
#         break
#
# print(res)

import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def isConnect(rect1, rect2):
    x1, y1, nx1, ny1 = arr[rect1]
    x2, y2, nx2, ny2 = arr[rect2]
    if x2 <= x1 <= nx2 and (y2 <= y1 <= ny2 or y2 <= ny1 <= ny2):
        return True
    elif x2 <= nx1 <= nx2 and (y2 <= y1 <= ny2 or y2 <= ny1 <= ny2):
        return True
    elif y2 <= y1 <= ny2 and (x2 <= x1 <= nx2 or x2 <= nx1 <= nx2):
        return True
    elif y2 <= ny1 <= ny2 and (x2 <= x1 <= nx2 or x2 <= nx1 <= nx2):
        return True
    return False

# arr = [[4, 4, 6, 6], [6, 6, 8, 8]]
# print(isConnect(0, 1))
# print(isConnect(1, 0))

def union_parent(parent, x, y):
    if isConnect(x, y):
        a = find_parent(parent, x)
        b = find_parent(parent, y)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

parent = [i for i in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        union_parent(parent, i, j)
        union_parent(parent, j, i)

res = len(set(parent))
for i in range(n):
    x, y, nx, ny = arr[i]
    if (y <= 0 <= ny and (x == 0 or nx == 0)) or ((y == 0 or ny == 0) and x <= 0 <= nx):
        res -= 1
        break

print(res)
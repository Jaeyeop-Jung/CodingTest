# TODO 틀림 다음엔 맞출 수 있다

# import sys
#
# input = sys.stdin.readline
#
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
# def union_parent(parent, x, y):
#     a = find_parent(parent, x)
#     b = find_parent(parent, y)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     parent = []
#     dic = {}
#     cnt = 0
#     for _ in range(n):
#         a, b = input().split()
#         if a not in dic:
#             dic[a] = cnt
#             parent.append(cnt)
#             cnt += 1
#         if b not in dic:
#             dic[b] = cnt
#             parent.append(cnt)
#             cnt += 1
#         union_parent(parent, dic[a], dic[b])
#
#         temp = 0
#         tempParent = find_parent(parent, dic[a])
#         for i in range(len(parent)):
#             if tempParent == find_parent(parent, i):
#                 temp += 1
#
#         print(temp)

import sys

input = sys.stdin.readline


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return network[a]
    parents[b] = a
    network[a] = network[a] + network[b]
    return network[a]


def find(k):
    if k != parents[k]:
        parents[k] = find(parents[k])
    return parents[k]


for _ in range(int(input())):
    parents = dict()
    network = dict()
    for _ in range(int(input())):
        a, b = input().rstrip().split()
        if parents.get(a) == None:
            parents[a] = a
            network[a] = 1
        if parents.get(b) == None:
            parents[b] = b
            network[b] = 1

        print(union(a, b))
# TODO 틀림 할 수 있다

import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [math.inf] * n
min_tree = [math.inf] * (4 * n)
max_tree = [0] * (4 * n)

def minUpdate(tree, start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = min(minUpdate(tree, start, mid, idx * 2), minUpdate(tree, mid + 1, end, idx * 2 + 1))
    return tree[idx]

def maxUpdate(tree, start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start + end) // 2
    left = maxUpdate(tree, start, mid, idx * 2)
    right = maxUpdate(tree, mid + 1, end, idx * 2 + 1)
    tree[idx] = max(left, right)
    return tree[idx]

def find_min(tree, start, end, idx, left, right):
    if right < start or end < left:
        return math.inf
    if left <= start and end <= right:
        return tree[idx]
    mid = (start + end) // 2
    return min(find_min(tree, start, mid, idx * 2, left, right), find_min(tree, mid + 1, end, idx * 2 + 1, left, right))

def find_max(tree, start, end, idx, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[idx]
    mid = (start + end) // 2
    return max(find_max(tree, start, mid, idx * 2, left, right), find_max(tree, mid + 1, end, idx * 2 + 1, left, right))

for i in range(n):
    arr[i] = int(input())
minUpdate(min_tree, 0, n - 1, 1)
maxUpdate(max_tree, 0, n - 1, 1)

for i in range(m):
    a, b = map(int, input().split())
    print(find_min(min_tree, 0, n - 1, 1, a - 1, b - 1), find_max(max_tree, 0, n - 1, 1, a - 1, b - 1))

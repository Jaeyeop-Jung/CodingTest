# TODO 틀림

import sys

input = sys.stdin.readline

n, m, = map(int, input().split())
arr = [0] * n
tree = [0] * (n * 4)


def update(tree, start, end, idx, k, v):
    if k < start or end < k:
        return
    if start == end:
        tree[idx] = arr[k]
        return
    mid = (start + end) // 2
    update(tree, start, mid, idx * 2, k, v)
    update(tree, mid + 1, end, idx * 2 + 1, k, v)
    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]


def find(tree, start, end, idx, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[idx]
    mid = (start + end) // 2
    return find(tree, start, mid, idx * 2, left, right) + find(tree, mid + 1, end, idx * 2 + 1, left, right)


for i in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        if c < b:
            b, c = c, b
        print(find(tree, 0, n - 1, 1, b - 1, c - 1))
    else:
        arr[b - 1] = c
        update(tree, 0, n - 1, 1, b - 1, c)

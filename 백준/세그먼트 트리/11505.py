import math
import sys
input = sys.stdin.readline

n, m, k, = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [0] * (1 << (int(math.ceil(math.log2(n))) + 1))


def init(tree, start, end, idx):
    if start == end:
        tree[idx] = arr[start] % 1000000007
        return tree[idx]
    mid = (start + end) // 2
    update1 = init(tree, start, mid, idx * 2)
    update2 = init(tree, mid + 1, end, idx * 2 + 1)
    tree[idx] = update1 * update2 % 1000000007
    return tree[idx] % 1000000007

def find(tree, start, end, idx, left, right):
    if right < start or end < left:
        return 1
    if left <= start and end <= right:
        return tree[idx] % 1000000007
    mid = (start + end) // 2
    return find(tree, start, mid, idx * 2, left, right) * find(tree, mid + 1, end, idx * 2 + 1, left, right) % 1000000007

def update(tree, start, end, idx, k, v):
    if k < start or end < k:
        return
    if start == end:
        tree[idx] = v % 1000000007
        return
    mid = (start + end) // 2
    update(tree, start, mid, idx * 2, k, v)
    update(tree, mid + 1, end, idx * 2 + 1, k, v)
    tree[idx] = tree[idx * 2] * tree[idx * 2 + 1]


init(tree, 0, len(arr) - 1, 1)

for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b - 1] = c
        update(tree, 0, len(arr) - 1, 1, b - 1, c)
    else:
        print(find(tree, 0, len(arr) - 1, 1, b - 1, c - 1))

import sys

input = sys.stdin.readline

n, q, = map(int, input().split())
arr = list(map(int, input().split()))
tree = [0] * (4 * n)


def init(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = init(start, mid, idx * 2) + init(mid + 1, end, idx * 2 + 1)
    return tree[idx]

def update(tree, start, end, idx, k, v):
    if k < start or end < k:    # 여기서 범위를 좁히면서
        return tree[idx]
    if start == end: # 결국에는 k == start == end가 맞을때로 수렴하기 때문에 성립 가능
        tree[idx] = v
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = update(tree, start, mid, idx * 2, k, v) + update(tree, mid + 1, end, idx * 2 + 1, k, v)
    return tree[idx]

def find(tree, start, end, idx, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:  # 범위 안에 구할 범위가 내포되어 있으면 그 구간 전체가 구할 범위기 때문에 바로 리턴한다
        return tree[idx]
    mid = (start + end) // 2
    return find(tree, start, mid, idx * 2, left, right) + find(tree, mid + 1, end, idx * 2 + 1, left, right)

init(0, n - 1, 1)
for _ in range(q):
    x, y, a, b = map(int, input().split())
    if y < x:
        x, y = y, x
    print(find(tree, 0, n - 1, 1, x - 1, y - 1))
    update(tree, 0, n - 1, 1, a - 1, b)

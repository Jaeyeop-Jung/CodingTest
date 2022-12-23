def init(start, end, index):
    # 가장 끝에 도달했으면 arr 삽입
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    # 좌측 노드와 우측 노드를 채워주면서 부모 노드의 값도 채워준다.
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return tree[index]

def prefix_sum(tree, curStart, curEnd, index, left, right):
    if curEnd < left or right < curStart:
        return 0
    if left <= curStart and curEnd <= right:
        return tree[index]
    mid = (curStart + curEnd) // 2
    return prefix_sum(tree, curStart, mid, index * 2, left, right) + prefix_sum(tree, mid + 1, curEnd, index * 2 + 1, left, right)

def update(tree, curStart, curEnd, index, k, v):
    if not curStart <= k <= curEnd:
        return
    tree[index] = tree[index] - arr[k] + v
    if curStart == curEnd == k:
        tree[index] = v
        return
    mid = (curStart + curEnd) // 2
    update(tree, curStart, mid, index * 2, k, v)
    update(tree, mid + 1, curEnd, index * 2 + 1, k, v)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tree = [0] * (len(arr) * 4)
init(0, 9, 1)
print(tree)
print(prefix_sum(tree, 0, 9, 1, 6, 9))
update(tree, 0, 9, 1, 0, 2)
print(tree)
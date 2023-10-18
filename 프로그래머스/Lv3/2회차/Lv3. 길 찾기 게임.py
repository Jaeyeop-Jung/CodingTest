from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)

def preOrder(dic, depths, idx, left, cur, right):
    # 가운데
    global pre
    pre.append(dic[depths[idx]][cur])
    if idx - 1 < 0:
        return

    # 왼쪽
    for x in dic[depths[idx - 1]]:
        if left < x < cur:
            preOrder(dic, depths, idx - 1, left, x, cur)
            break

    # 오른쪽
    for x in dic[depths[idx - 1]]:
        if cur < x < right:
            preOrder(dic, depths, idx - 1, cur, x, right)
            break

def postOrder(dic, depths, idx, left, cur, right):
    # 왼쪽
    for x in dic[depths[idx - 1]]:
        if left < x < cur:
            postOrder(dic, depths, idx - 1, left, x, cur)
            break

    # 오른쪽
    for x in dic[depths[idx - 1]]:
        if cur < x < right:
            postOrder(dic, depths, idx - 1, cur, x, right)
            break

    # 가운데
    global post
    post.append(dic[depths[idx]][cur])

pre = []
post = []
def solution(nodeinfo):
    global pre, post
    pre, post = [], []
    dic = defaultdict(dict)
    for i, v in enumerate(nodeinfo):
        x, y = v
        dic[y][x] = i + 1

    depths = sorted(dic.keys())
    preOrder(dic, depths, len(depths) - 1, -1, list(dic[depths[-1]].keys())[0], 100_001)
    postOrder(dic, depths, len(depths) - 1, -1, list(dic[depths[-1]].keys())[0], 100_001)
    return pre, post

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
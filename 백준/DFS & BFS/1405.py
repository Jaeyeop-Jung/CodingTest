# TODO 틀림 아이디어는 맞았다 구현만 조금 신경써라

import sys

sys.setrecursionlimit(10 ** 6)

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, east, west, south, north = map(int, input().split())
direction = [east, south, west, north]

res = 0
def dfs(visited, r, c, percent, idx):
    global res
    if idx == n:
        res += percent
        return

    for i in range(4):
        if 0 < direction[i]:
            movedR, movedC = r + dR[i], c + dC[i]
            if (movedR, movedC) not in visited:
                visited[(movedR, movedC)] = True
                dfs(visited, movedR, movedC, percent * direction[i] / 100, idx + 1)
                del visited[(movedR, movedC)]

dfs({(0, 0): True}, 0, 0, 1, 0)
print(res)
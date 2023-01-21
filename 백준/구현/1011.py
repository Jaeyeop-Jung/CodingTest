# TODO 틀림 잘 생각해봐라


import sys
from collections import deque
input = sys.stdin.readline

# dMove = [-1, 0, 1]

t = int(input())
for _ in range(t):
    x, y, = map(int, input().split())
    # q = deque()
    # q.append([x, 0, 0])
    # while q:
    #     cur, moveStd, cnt, = q.popleft()
    #     if cur == y and moveStd == 1:
    #         print(cnt)
    #         break
    #     for i in range(3):
    #         nextMove = moveStd + dMove[i]
    #         if nextMove <= 0:
    #             continue
    #         next = cur + nextMove
    #         if y < next:
    #             continue
    #         if next == y and nextMove != 1:
    #             continue
    #         q.append([next, nextMove, cnt + 1])

    cnt = 0


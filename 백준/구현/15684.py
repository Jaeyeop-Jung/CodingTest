import sys
from itertools import combinations

input = sys.stdin.readline

n, m, h = map(int, input().split())
ladder = [[False] * n for _ in range(h)]
for i in range(m):
    a, b = map(int, input().split())
    ladder[a - 1][b - 1] = True

def start():
    for cur in range(n):
        temp = cur
        for r in range(h):
            if temp < n and ladder[r][temp]:
                temp += 1
            elif 0 <= temp - 1 and ladder[r][temp - 1]:
                temp -= 1
        if cur != temp:
            return False
    return True

allLadder = [[r, c] for r in range(h) for c in range(n)]
# for addNum in range(4):
#     for cases in combinations(allLadder, addNum):
#         cnt = m
#         tempAdd = []
#         for case in cases:
#             r, c, = case
#             if not ladder[r][c]:
#                 if 0 <= c - 1 and ladder[r][c - 1]:
#                     break
#                 if c + 1 < n and ladder[r][c + 1]:
#                     break
#                 ladder[r][c] = True
#                 tempAdd.append([r, c])
#                 cnt += 1
#             else:
#                 break
#         else:
#             if start():
#                 print(addNum)
#                 exit()
#         for case in tempAdd:
#             r, c, = case
#             ladder[r][c] = False

def dfs(target, cnt, cur):
    if target == cnt:
        return
    elif cnt < target:
        if start():
            # print(cnt)
            # exit()
            global ans
            ans = min(ans, cnt)
            return
    for next in range(cur, len(allLadder)):
        r, c = allLadder[next]
        if not ladder[r][c]:
            if 0 <= c - 1 and ladder[r][c - 1]:
                continue
            if c + 1 < n and ladder[r][c + 1]:
                continue
            ladder[r][c] = True
            dfs(target, cnt + 1, next)
            ladder[r][c] = False
ans = 4
dfs(4, 0, 0)
print(ans if ans < 4 else -1)

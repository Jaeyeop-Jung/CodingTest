# import math
# import random
# import sys
#
# input = sys.stdin.readline
#
# # n = int(input())
# # for _ in range(n):
# def sol1(m, n, x, y):
#     # m, n, x, y, = map(int, input().split())
#     if m == n:
#         return x if x == y else -1
#         # print(x if x == y else -1)
#         # continue
#
#     if n < m:
#         n, m = m, n
#         x, y = y, x
#     gcd = math.gcd(m, n)
#     maxGcd = gcd * (m // gcd) * (n // gcd)
#     diff = abs(m - n)
#     if m == x and n == y:
#         return maxGcd
#         # print(maxGcd)
#         # continue
#     # print(maxGcd)
#
#     eX, eY = x, y
#     while eY != 1:
#         eX -= 1
#         eY -= 1
#         if eX == 0:
#             eX = m
#         if eY == 0:
#             eY = n
#
#     cost = 1
#     curX, curY = 1, 1
#     while cost <= maxGcd:
#         if curX == eX:
#             break
#         curX += diff
#         if m < curX:
#             curX %= m
#         cost += n
#     else:
#         return -1
#         # print(-1)
#         # continue
#
#     while not (curX == x and curY == y):
#         curX %= m
#         curY %= n
#         cost += 1
#         curX = curX + 1
#         curY = curY + 1
#
#     # print(cost if cost < maxGcd else -1)
#     return cost if cost < maxGcd else -1
#
# def sol2(m, n, x, y):
#     def calculate(m, n, x, y):
#         k = x #k를 x로 초기화
#         while k <= m * n: #k의 범위는 m*n을 넘을 수 없기에
#             if (k - x) % m == 0 and (k - y) % n == 0: #2개의 조건을 만족하는 k값을 찾는다.
#                 return k
#             k += m #k-x가 m의 배수이기 때문에 k는 x로 초기화해주었기 때문에 m만 더해준다.
#         return -1
#
#     return calculate(m, n, x, y)
#
# while True:
#     m, n = random.randrange(1, 40000), random.randrange(1, 40000)
#     x, y = random.randrange(1, m), random.randrange(1, n)
#     if sol1(m, n, x, y) != sol2(m, n, x, y):
#         print(m, n, x, y)

import math
import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m, n, x, y, = map(int, input().split())
    if m == n:
        print(x if x == y else -1)
        continue

    if n < m:
        n, m = m, n
        x, y = y, x
    gcd = math.gcd(m, n)
    maxGcd = gcd * (m // gcd) * (n // gcd)
    diff = abs(m - n)
    if m == x and n == y:
        print(maxGcd)
        continue
    # print(maxGcd)

    eX, eY = x, y
    while eY != 1:
        eX -= 1
        eY -= 1
        if eX == 0:
            eX = m
        if eY == 0:
            eY = n

    cost = 1
    curX, curY = 1, 1
    while cost <= maxGcd:
        if curX == eX:
            break
        curX += diff
        if m < curX:
            curX %= m
        if curX == 0:
            curX = m
        cost += n
    else:
        print(-1)
        continue

    while not (curX == x and curY == y):
        curX %= m
        curY %= n
        cost += 1
        curX = curX + 1
        curY = curY + 1

    print(cost if cost < maxGcd else -1)
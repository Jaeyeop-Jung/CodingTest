# TODO 틀림

import math

n, red, green, blue = map(int, input().split())

def recur(idx, color):
    if idx == n + 1:
        return 1

    temp = 0
    # 1개만 쓸 때
    for i in range(3):
        if idx <= color[i]:
            color[i] -= idx
            temp += recur(idx + 1, color)
            color[i] += idx

    # 2개만 쓸 때
    if idx % 2 == 0:
        for i in range(3):
            for j in range(i + 1, 3):
                if color[i] < idx // 2 or color[j] < idx // 2:
                    continue
                multi1 = math.comb(color[i], idx // 2)
                multi2 = math.comb(color[j], idx // 2)
                color[i] -= idx // 2
                color[j] -= idx // 2
                temp += recur(idx + 1, color) * math.comb(idx, idx // 2)
                color[i] += idx // 2
                color[j] += idx // 2

    # 3개
    if idx % 3 == 0 and idx // 3 <= color[0] and idx // 3 <= color[1] and idx // 3 <= color[2]:
        multi1 = math.comb(color[0], idx // 2)
        multi2 = math.comb(color[1], idx // 2)
        multi3 = math.comb(color[2], idx // 2)
        color[0] -= idx // 3
        color[1] -= idx // 3
        color[2] -= idx // 3
        temp += recur(idx + 1, color) * math.comb(idx, idx // 3) * math.comb(idx - idx // 3, idx // 3)
        color[0] += idx // 3
        color[1] += idx // 3
        color[2] += idx // 3

    return temp

print(recur(1, [red, green, blue]))
# TODO 틀림

import math
from itertools import product
from collections import deque
import heapq

def move(stair, peopleNums):
    time = []
    eR, eC, _ = stair
    for num in peopleNums:
        r, c, = people[num]
        time.append(abs(eR - r) + abs(eC - c))
    time.sort()
    return time


def simul(per):
    times = deque(move(stairs[0], [i for i in range(len(per)) if per[i] == 0]))
    curStair = []
    _, _, length = stairs[0]
    time = 0
    while times or curStair:
        while times and len(curStair) < 3 and times[0] < time:
            times.popleft()
            heapq.heappush(curStair, length + time)
            # curStair.append(length + time + 1)
        while curStair and curStair[0] == time:
            # curStair.popleft()
            heapq.heappop(curStair)
        while times and len(curStair) < 3 and times[0] < time:
            times.popleft()
            # curStair.append(length + time)
            heapq.heappush(curStair, length + time)
        time += 1
    res = time - 1

    times = deque(move(stairs[1], [i for i in range(len(per)) if per[i] == 1]))
    curStair = []
    _, _, length = stairs[1]
    time = 0
    while times or curStair:
        while times and len(curStair) < 3 and times[0] < time:
            times.popleft()
            heapq.heappush(curStair, length + time)
            # curStair.append(length + time + 1)
        while curStair and curStair[0] == time:
            # curStair.popleft()
            heapq.heappop(curStair)
        while times and len(curStair) < 3 and times[0] < time:
            times.popleft()
            # curStair.append(length + time)
            heapq.heappush(curStair, length + time)
        time += 1
    res = max(res, time - 1)
    return res

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    stairs = []
    peopleNum = 0
    people = {}
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 1:
                people[peopleNum] = [r, c]
                peopleNum += 1
            elif arr[r][c] != 0:
                stairs.append((r, c, arr[r][c]))

    result = math.inf
    for per in product([0, 1], repeat=peopleNum):
        result = min(result, simul(per))
    print(f'#{tc} {result}')
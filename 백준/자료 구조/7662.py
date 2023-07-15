# TODO 틀림 더 고민해봐 할 수 있다

import heapq
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    q = int(input())
    visited = [False] * q
    minH, maxH = [], []
    for i in range(q):
        command, num, = input().split()
        if command == 'I':
            heapq.heappush(minH, (int(num), i))
            heapq.heappush(maxH, (-int(num), i))
        else:
            if int(num) == 1:
                while maxH and visited[maxH[0][1]]:
                    heapq.heappop(maxH)
                if maxH:
                    _, idx = heapq.heappop(maxH)
                    visited[idx] = True
            else:
                while minH and visited[minH[0][1]]:
                    heapq.heappop(minH)
                if minH:
                    _, idx = heapq.heappop(minH)
                    visited[idx] = True

    while maxH and visited[maxH[0][1]]:
        heapq.heappop(maxH)
    while minH and visited[minH[0][1]]:
        heapq.heappop(minH)

    if maxH:
        print(-maxH[0][0], minH[0][0])
    else:
        print('EMPTY')
# TODO 틀림 풀 수 있다 잘 생각해봐

import sys

input = sys.stdin.readline

c, n, = map(int, input().split())
chicken = sorted([int(input()) for _ in range(c)])
cow = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))

visited = [False] * c
for start, end in cow:
    for i in range(c):
        if start <= chicken[i] <= end and not visited[i]:
            visited[i] = True
            break

print(visited.count(True))


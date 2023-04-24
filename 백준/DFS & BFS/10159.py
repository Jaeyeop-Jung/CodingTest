from collections import defaultdict
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
dic = defaultdict(set)
for _ in range(m):
    win, lose, = map(int, input().split())
    dic[win].add(lose)

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    visited[i] = True

    for j in range(1, n + 1):
        if i == j:
            continue
        q = deque([j])
        tempVisited = [False] * (n + 1)
        tempVisited[j] = True
        flag = False
        while q:
            cur = q.popleft()
            for next in dic[cur]:
                if next == i:
                    visited[j] = True
                    flag = True
                    break
                if not tempVisited[next]:
                    tempVisited[next] = True
                    q.append(next)
            if flag:
                break

    q = deque([i])
    while q:
        cur = q.popleft()
        for next in dic[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)

    print(n - visited.count(True))

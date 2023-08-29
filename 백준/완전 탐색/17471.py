import math
from itertools import product
from collections import deque

def isConnected(team):
    q = deque()
    q.append(team[0])
    visited = [False] * n
    visited[team[0]] = True
    while q:
        cur = q.popleft()
        for next in range(len(graph[cur])):
            if not graph[cur][next] or next not in team or visited[next]:
                continue
            visited[next] = True
            q.append(next)
    for member in team:
        if not visited[member]:
            return False
    return True


def simul(per):
    teamZero = [i for i in range(len(per)) if per[i] == 0]
    teamOne = [i for i in range(len(per)) if per[i] == 1]

    # 지역구에 유권자 없을 때
    if len(teamZero) == len(per) or len(teamOne) == len(per):
        return

    if isConnected(teamZero) and isConnected(teamOne):
        global res
        teamZeroScore = sum([scores[i] for i in teamZero])
        teamOneScore = sum([scores[i] for i in teamOne])
        res = min(res, abs(teamOneScore - teamZeroScore))

n = int(input())
scores = list(map(int, input().split()))
graph = [[0] * n for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(1, len(temp)):
        graph[i][temp[j] - 1] = 1
        graph[temp[j] - 1][i] = 1

res = math.inf
for per in product([0, 1], repeat=n):
    simul(per)
print(res if res != math.inf else -1)
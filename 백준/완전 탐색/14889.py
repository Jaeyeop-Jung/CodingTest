import math
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

rang = [i for i in range(n)]
result = math.inf
for case in combinations(rang, n // 2):
    startTeamScore = 0  # 스타트팀
    for i in case:
        for j in case:
            if i != j:
                startTeamScore += arr[i][j]

    otherTeamScore = 0
    otherTeam = rang[:]
    for i in case:
        otherTeam.remove(i)
    for i in otherTeam:
        for j in otherTeam:
            if i != j:
                otherTeamScore += arr[i][j]

    result = min(result, abs(startTeamScore - otherTeamScore))
print(result)

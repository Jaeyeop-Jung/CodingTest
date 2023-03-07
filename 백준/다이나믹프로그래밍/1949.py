# TODO 틀림
# 이 문제의 경우 우수 = ㅇ, 평범 = ㄴ라고 할 때
# ㄴㄴㄴㅇ와 같이 ㄴ가 연속적인 경우가 왜 가능한가 의문점을 가짐
# 그리디적으로 ㄴㄴㄴㅇ보다 ㅇㄴㄴㅇ 또는 ㄴㅇㄴㅇ와 같이 어떻게든 마을을 하나 우수로 하는 게
# 더 max값이기 때문에 인구수는 음수가 아니니까.
# max로 dp를 업데이트 해줄 수 있다

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def village(start, dp, visited):
    visited[start] = True

    for i in tree[start]:
        if not visited[i]:
            village(i, dp, visited)
            dp[start][0] += max(dp[i][0], dp[i][1])
            dp[start][1] += dp[i][0]


n = int(input())
people = [0] + list(map(int, input().split()))
tree = [[] for i in range(n + 1)]
visited = [0 for i in range(n + 1)]
dp = [[0, people[i]] for i in range(n + 1)]  # [i][0]: 우수마을 x, [i][1]: 우수마을
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
village(1, dp, visited)
print(max(dp[1][0], dp[1][1]))
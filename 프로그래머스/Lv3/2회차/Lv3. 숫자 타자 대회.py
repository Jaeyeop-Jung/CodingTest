import math
import sys
sys.setrecursionlimit(10 ** 8)

board = [
    [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
    [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
    [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
    [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
    [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
    [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
    [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
    [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
    [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
    [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]
]

# def solution(numbers):
#     n = len(numbers)
#     dp = [[[math.inf] * 10 for _ in range(10)] for _ in range(n + 1)]
#     dp[0][4][6] = 0
#
#     for i in range(1, n + 1):
#         next = int(numbers[i - 1])
#         for left in range(10):
#             for right in range(10):
#                 if next != left:
#                     dp[i][left][next] = min(dp[i][left][next], dp[i - 1][left][right] + board[right][next])
#                 if next != right:
#                     dp[i][next][right] = min(dp[i][next][right], dp[i - 1][left][right] + board[left][next])
#
#     return min(map(min, dp[-1]))

def dfs(numbers, dp, idx, left, right):
    if idx == len(numbers) + 1:
        return

    next = int(numbers[idx - 1])
    if left != next and dp[idx - 1][left][right] + board[right][next] < dp[idx][left][next]:
        dp[idx][left][next] = dp[idx - 1][left][right] + board[right][next]
        dfs(numbers, dp, idx + 1, left, next)
    if right != next and dp[idx - 1][left][right] + board[left][next] < dp[idx][next][right]:
        dp[idx][next][right] = dp[idx - 1][left][right] + board[left][next]
        dfs(numbers, dp, idx + 1, next, right)

def solution(numbers):
    n = len(numbers)
    dp = [[[math.inf] * 10 for _ in range(10)] for _ in range(n + 1)]
    dp[0][4][6] = 0

    dfs(numbers, dp, 1, 4, 6)

    return min(map(min, dp[-1]))

print(solution('5123'))
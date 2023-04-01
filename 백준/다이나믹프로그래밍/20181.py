# TODO 틀림

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# board = [[0] * n for _ in range(n)]
# dp = [[0] * n for _ in range(n)]
# for r in range(n):
#     board[r][r] = arr[r]
#     dp[r][r] = max(0, board[r][r] - k)
#     if k <= board[r][r]:
#         dp[r][r] = board[r][r] - k
#         continue
#     for c in range(r + 1, n):
#         board[r][c] = board[r][c - 1] + arr[c]
#         if k <= board[r][c - 1] + arr[c]:
#             dp[r][c] = board[r][c - 1] + arr[c] - k
#             break
#
# r, c = 0, 1
# for _ in range(n - 1):
#     dp[r][c] = max(dp[r][c - 1] + dp[r + 1][c], dp[r][c])
#     r += 1
#     c += 1
#
# for right in range(2, n):
#     for left in range(n):
#         if n <= left + right:
#             break
#         for k in range(left, left + right):
#             dp[left][left + right] = max(dp[left][left + right], dp[left][k] + dp[k + 1][left + right])
#
# print(dp[0][-1])

dp = [0] * n
left, right = 0, 0
total = arr[0]
dp[0] = max(0, total - k)
while True:
    if total < k:
        right += 1
        if n <= right:
            break
        total += arr[right]
    else:
        if left == 0:
            dp[right] = max(dp[right], total - k, dp[right - 1])
        else:
            dp[right] = max(dp[right], dp[left - 1] + total - k, dp[right - 1], dp[left - 1])
        total -= arr[left]
        left += 1

print(max(dp))
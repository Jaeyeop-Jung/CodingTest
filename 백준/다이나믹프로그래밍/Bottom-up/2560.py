# TODO 틀림

a, b, d, n = map(int, input().split())
dp = [0] * (n + 1)
cur = [0] * (n + 1)
dp[0] = 1
dp[a] = 1
for i in range(a):
    cur[i] = 1
cur[a] = 2

left, right = -(b - a - 1), 0
# left, right = -4, 0
added = 1
for i in range(a + 1, n):
    if 0 <= left:
        added -= dp[left]
    left += 1
    # added += dp[left]
    right += 1
    added += dp[right]

    dp[i] = added
    cur[i] = (cur[i - 1] + added) % 1000

print(cur[-2])
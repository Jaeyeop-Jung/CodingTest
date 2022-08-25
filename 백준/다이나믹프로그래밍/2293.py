# TODO https://www.youtube.com/watch?v=2IkdAk1Loek&ab_channel=%EC%A7%84%EC%93%B0%EC%BD%94%EB%94%A9

n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
coin.sort()

dp = [0] * (k + 1)
dp[0] = 1
for i in coin:
    for j in range(i, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
print(dp[k])


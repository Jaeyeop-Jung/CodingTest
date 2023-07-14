# TODO 틀림 잘 생각해봐 점화식 세우기를

while True:
    t = int(input())
    if t == 0:
        break

    # print(dfs({}, t, 0))

    dp = [[0] * ((t + 1) * 2) for _ in range(t + 1)]
    dp[t][0] = 1
    for w in range(t, -1, -1):
        for h in range(t, -1, -1):
            if 0 <= h - 1:
                dp[w][h - 1] += dp[w][h]
            dp[w - 1][h + 1] += dp[w][h]

    print(dp[0][0])
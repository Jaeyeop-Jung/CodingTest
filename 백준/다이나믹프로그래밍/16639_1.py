import math
import re

n = int(input())
origin = input()

num = list(map(int, re.findall('\d+', origin)))
operator = re.findall('\D+', origin)

numLength = len(num)
dp = [[[-math.inf, math.inf] for _ in range(numLength)] for _ in range(numLength)]
for i in range(numLength):
    dp[i][i][0] = num[i]
    dp[i][i][1] = num[i]

for c in range(1, numLength):
    for r in range(numLength):
        if numLength <= r + c:
            continue
        for separator in range(r, r + c):
            dp[r][r + c][0] = max(dp[r][r + c][0], eval(str(dp[r][separator][0]) + operator[separator] + str(dp[separator + 1][r + c][0])))
            dp[r][r + c][0] = max(dp[r][r + c][0], eval(str(dp[r][separator][0]) + operator[separator] + str(dp[separator + 1][r + c][1])))
            dp[r][r + c][0] = max(dp[r][r + c][0], eval(str(dp[r][separator][1]) + operator[separator] + str(dp[separator + 1][r + c][0])))
            dp[r][r + c][0] = max(dp[r][r + c][0], eval(str(dp[r][separator][1]) + operator[separator] + str(dp[separator + 1][r + c][1])))

            dp[r][r + c][1] = min(dp[r][r + c][1], eval(str(dp[r][separator][1]) + operator[separator] + str(dp[separator + 1][r + c][1])))
            dp[r][r + c][1] = min(dp[r][r + c][1], eval(str(dp[r][separator][1]) + operator[separator] + str(dp[separator + 1][r + c][0])))
            dp[r][r + c][1] = min(dp[r][r + c][1], eval(str(dp[r][separator][0]) + operator[separator] + str(dp[separator + 1][r + c][1])))
            dp[r][r + c][1] = min(dp[r][r + c][1], eval(str(dp[r][separator][0]) + operator[separator] + str(dp[separator + 1][r + c][0])))

print(dp[0][-1][0])
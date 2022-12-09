import math
import sys

input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
price.pop()

dp = [math.inf] * (n - 1)
dp[0] = price[0] * distance[0]
minPrice = price[0]
for i in range(1, len(dp)):
    minPrice = min(minPrice, price[i])
    dp[i] = dp[i-1] + minPrice * distance[i]

print(dp[-1])
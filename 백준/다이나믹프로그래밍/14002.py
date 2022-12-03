# TODO 틀림 잘 생각 해봐 맞았는데 틀리네;

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
# for i in range(1, n):
#     for j in range(i):



order = max(dp)
result = []
for i in range(n - 1, -1, -1):
    if dp[i] == order:
        order -= 1
        result.append(arr[i])

print(*reversed(result))
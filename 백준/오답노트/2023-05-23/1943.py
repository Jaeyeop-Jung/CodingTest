import sys

input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    total = sum([i[0] * i[1] for i in arr])
    if total % 2 == 1:
        print(0)
        continue

    total //= 2
    dp = [False] * (total + 1)
    dp[0] = True
    flag = False
    for price, num, in arr:
        for i in range(total, price - 1, -1):
            if dp[i - price]:
                for j in range(num):
                    if total < i + price * j:
                        break
                    dp[i + price * j] = True
                    if i + price * j == total:
                        flag = True
                        break
        if flag:
            break
    if flag:
        print(1)
    else:
        print(0)


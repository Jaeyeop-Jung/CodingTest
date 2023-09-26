
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

memo = [0] * 366
for start, end in arr:
    for i in range(start, end + 1):
        memo[i] += 1

flag = False
start = -1
res = 0
maxi = 0
for i in range(len(memo)):
    if not flag and memo[i] != 0:
        flag = True
        start = i
    elif flag and memo[i] == 0:
        res += (i - start) * maxi
        flag = False
        start = -1
        maxi = 0
    maxi = max(maxi, memo[i])

if flag:
    res += (365 + 1 - start) * maxi

print(res)
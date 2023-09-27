from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

cur = []
index = [-1] * n
for i in range(n):
    if not cur:
        cur.append(arr[i])
        index[i] = 0
    elif cur[-1] < arr[i]:
        cur.append(arr[i])
        index[i] = len(cur) - 1
    else:
        idx = bisect_left(cur, arr[i])
        index[i] = idx
        cur[idx] = arr[i]

print(max(index) + 1)
res = []
cnt = max(index)
for i in range(len(index) - 1, -1, -1):
    if index[i] == cnt:
        cnt -= 1
        res.append(arr[i])
print(*list(reversed(res)))
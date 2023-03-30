n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

start, end = 0, 1_000_000_000
res = 0
while start <= end:
    mid = (start + end) // 2
    temp = m - 1
    cur = arr[0]
    for i in range(1, n):
        if mid <= arr[i] - cur:
            temp -= 1
            cur = arr[i]
    if temp <= 0:
        res = max(res, mid)
        start = mid + 1
    else:
        end = mid - 1

print(res)

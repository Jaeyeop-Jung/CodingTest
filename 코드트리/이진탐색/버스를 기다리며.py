
n, m, c = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def isAvailable(wait):
    cnt = 0
    cur = []
    for i in range(len(arr)):
        if not cur or arr[i] - arr[cur[0]] <= wait:
            cur.append(i)
        else:
            cnt += 1
            cur = [i]

        if c <= len(cur):
            cnt += 1
            cur = []
    if cur:
        cnt += 1

    return cnt <= m

start, end = 0, 10 ** 9
res = 10 ** 9
while start <= end:
    mid = (start + end) // 2
    if isAvailable(mid):
        end = mid - 1
        res = min(res, mid)
    else:
        start = mid + 1

print(res)
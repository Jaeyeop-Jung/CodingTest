
target, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
arr.sort(key=lambda x: (x[0], x[1]))

def isAvailable(term):
    cur = arr[0][0]
    cnt = 1
    for i in range(len(arr)):
        while True:
            if cur + term <= arr[i][0]:
                cnt += 1
                cur = arr[i][0]
            elif arr[i][0] < cur + term <= arr[i][1]:
                cnt += 1
                cur += term
            else:
                break
    return target <= cnt

start, end = 0, 10 ** 18
while start <= end:
    mid = (start + end) // 2
    if isAvailable(mid):
        start = mid + 1
    else:
        end = mid - 1

print(end)
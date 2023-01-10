# TODO 틀림 https://deok2kim.tistory.com/109

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def getCnt():
    cnt = 0
    total = 0
    for i in range(len(arr)):
        if total + arr[i] <= mid:
            total += arr[i]
        else:
            cnt += 1
            total = arr[i]
    return cnt

start = max(arr)
end = sum(arr)
while start <= end:
    mid = (start + end) // 2
    cnt = getCnt()
    if cnt < m:
        end = mid - 1
    else:
        start = mid + 1

print(start)

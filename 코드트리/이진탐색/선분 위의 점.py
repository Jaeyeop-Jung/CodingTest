n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
for _ in range(m):
    start, end = map(int, input().split())
    left, right = 0, n - 1
    minIdx = n
    while left <= right:
        mid = (left + right) // 2
        if start <= arr[mid]:
            right = mid - 1
            minIdx = min(minIdx, mid)
        else:
            left = mid + 1

    maxIdx = n
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if end < arr[mid]:
            right = mid - 1
            maxIdx = min(maxIdx, mid)
        else:
            left = mid + 1

    print(maxIdx - minIdx)
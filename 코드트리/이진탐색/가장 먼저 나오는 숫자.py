n, m = map(int, input().split())
arr = list(map(int, input().split()))
targets = list(map(int, input().split()))

for target in targets:
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if target <= arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if start < 0 or n <= start:
        print(-1)
        continue
    print(start + 1 if arr[start] == target else -1)

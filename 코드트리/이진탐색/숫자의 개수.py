n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    target = int(input())
    start, end = 0, n - 1
    # bis_right = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    left, right = 0, n - 1
    bis_left = -1
    while left <= right:
        mid = (left + right) // 2
        if target <= arr[mid]:
            right = mid - 1
            bis_left = mid
        else:
            left = mid + 1

    if start == -1 or bis_left == -1:
        print(0)
    else:
        print(start - bis_left)

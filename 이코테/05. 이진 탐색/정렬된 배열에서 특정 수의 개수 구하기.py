import bisect

n, m = map(int ,input().split())
arr = list(map(int, input().split()))
left = bisect.bisect_left(arr, m)
right = bisect.bisect_right(arr, m)
print(right - left)

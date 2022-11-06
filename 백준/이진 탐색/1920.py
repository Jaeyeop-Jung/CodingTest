
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
targetArr = list(map(int, input().split()))

arr.sort()
for target in targetArr:
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    if len(arr) <= start or arr[start] != target:
        print(0)
    else:
        print(1)

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

arr.sort()
result = []
for target in targets:
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    if n <= start or arr[start] != target:
        result.append(0)
    else:
        result.append(1)

for i in result:
    print(i, end=' ')
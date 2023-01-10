n, l, = map(int, input().split())
arr = sorted(list(map(int, input().split())))

idx = 0
cnt = 0
while idx < len(arr):
    start = arr[idx] - 0.5
    end = start + l
    cnt += 1
    idx += 1
    while idx < len(arr):
        if start <= arr[idx] - 0.5 and arr[idx] + 0.5 <= end:
            idx += 1
        else:
            break
print(cnt)

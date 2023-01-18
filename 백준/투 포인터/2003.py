n, m = map(int, input().split())
arr = list(map(int, input().split()))

cur = arr[0]
result = 0
left = 0
right = 0
while right < len(arr):
    if cur == m:
        result += 1
        cur -= arr[left]
        left += 1
        if len(arr) <= left:
            break
    elif cur < m:
        right += 1
        if len(arr) <= right:
            break
        cur += arr[right]
    else:
        cur -= arr[left]
        left += 1
        if len(arr) <= left:
            break

print(result)

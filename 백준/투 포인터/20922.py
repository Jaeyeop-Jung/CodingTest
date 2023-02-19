from collections import defaultdict

n, k, = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
result = 0
cur = defaultdict(int)
cur[arr[0]] = 1

while True:
    result = max(result, right - left + 1)
    right += 1
    if len(arr) <= right:
        break
    cur[arr[right]] += 1

    if k < cur[arr[right]]:
        while k < cur[arr[right]]:
            cur[arr[left]] -= 1
            left += 1


print(result)
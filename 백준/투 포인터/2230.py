import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
result = abs(arr[-1] - arr[0])
left_idx = 0
right_idx = 1
while left_idx < n and right_idx < n:
    temp = abs(arr[right_idx] - arr[left_idx])
    if m <= temp:
        result = min(result, temp)

    if temp == m:
        break
    elif temp < m and right_idx < n:
        right_idx += 1
    elif m < temp:
        left_idx += 1

print(result)

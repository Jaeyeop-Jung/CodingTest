import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[0], x[1]))
result = 1
left, right = arr[0][0], arr[0][1]
flag = False
for i in range(1, len(arr)):
    if arr[i][1] < right:
        left, right = arr[i][0], arr[i][1]
        continue

    if right <= arr[i][0]:
        result += 1
        left, right = arr[i][0], arr[i][1]

print(result)

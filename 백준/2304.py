# TODO 틀림 맞아라 이건 좀

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[0])
heights = [i[1] for i in arr]
maxHeight = max(heights)
index = heights.index(maxHeight)
lastIndex = len(arr) - 1
for i in range(len(arr) - 1, -1, -1):
    if arr[i][1] == maxHeight:
        lastIndex = i
        break

result = 0
x, y = arr[0]
for i in range(index + 1):
    if y < arr[i][1]:
        result += (arr[i][0] - x) * y
        x, y = arr[i]

x, y = arr[-1]
for i in range(len(arr) - 1, lastIndex - 1, -1):
    if y < arr[i][1]:
        result += (x - arr[i][0]) * y
        x, y = arr[i]

if index == lastIndex:
    result += arr[index][1]
else:
    result += (arr[lastIndex][0] - arr[index][0] + 1) * maxHeight
print(result)
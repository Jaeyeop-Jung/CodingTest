import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

# 로직
arr.sort(key=lambda x: x[0])
stack = [arr[0][1]]
index = [[arr[0][0], 1]]
for i in range(1, n):
    if stack[-1] < arr[i][1]:
        stack.append(arr[i][1])
        index.append([arr[i][0], len(stack)])
    else:
        left = bisect_left(stack, arr[i][1])
        stack[left] = arr[i][1]
        index.append([arr[i][0], left + 1])

# 출력
print(n - len(stack))
result = [i[0] for i in arr]
idx = max([i[1] for i in index])
for i in range(len(index) - 1, -1, -1):
    if idx == index[i][1]:
        result.remove(index[i][0])
        idx -= 1
result.sort()
for i in result:
    print(i, end=' ')
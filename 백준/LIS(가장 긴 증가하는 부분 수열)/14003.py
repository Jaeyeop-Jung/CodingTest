# TODO 틀림 https://velog.io/@jengyoung/baekjoon1400214003
from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

stack = [arr[0]]
LIS = [1]

# 로직
for i in range(1, len(arr)):
    if stack[-1] < arr[i]:
        stack.append(arr[i])
        LIS.append(len(stack))
    else:
        start = bisect_left(stack, arr[i])
        stack[start] = arr[i]
        LIS.append(start + 1)

# 출력부
print(len(stack))
index = max(LIS)
LIS_result = []
for i in range(len(LIS) - 1, -1, -1):
    if index == LIS[i]:
        LIS_result.append(arr[i])
        index -= 1
LIS_result.sort()
for i in LIS_result:
    print(i, end=' ')

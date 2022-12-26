# TODO 틀림 맞을 수 있었는데 잘 해봐라

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr = [[i, arr[i]] for i in range(len(arr))]

result = [-1] * len(arr)
stack = []
for i in range(len(arr)):
    while stack and stack[-1][1] < arr[i][1] and stack[-1][0] < arr[i][0]:
        idx, v = stack.pop()
        result[idx] = arr[i][1]
    stack.append(arr[i])

print(*result)

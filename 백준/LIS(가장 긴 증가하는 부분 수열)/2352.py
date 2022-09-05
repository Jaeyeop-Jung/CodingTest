from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

stack = [arr[0]]

for i in range(1, len(arr)):
    if stack[-1] < arr[i]:
        stack.append(arr[i])
    else:
        stack[bisect_left(stack, arr[i])] = arr[i]

print(len(stack))
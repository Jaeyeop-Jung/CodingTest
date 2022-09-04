# TODO 틀림 https://hongcoding.tistory.com/14

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = list(map(int, input().split()))
#
# dp = [1] * n
#
# for i in range(1, n):
#     for j in range(0, i):
#         if arr[j] < arr[i]:
#             dp[i] = max(dp[i], dp[j] + 1)
#
# print(max(dp))

# from bisect import bisect_left
#
# n = int(input())
# array = list(map(int, input().split()))
# stack = [0]
#
# for i in array:
#     if stack[-1] < i:
#         stack.append(i)
#     else:
#         left = bisect_left(stack, i)
#         stack[left] = i
#
# print(len(stack) - 1)

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
stack = [arr[0]]

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if stack[mid] == target:
            return mid
        elif stack[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

for i in range(1, len(arr)):
    if stack[-1] < arr[i]:
        stack.append(arr[i])
    else:
        stack[binary_search(arr[i], 0, len(stack) - 1)] = arr[i]

print(len(stack))
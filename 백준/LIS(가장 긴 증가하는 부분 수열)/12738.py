
# n = int(input())
# arr = list(map(int, input().split()))
#
# dp = [1] * n
# for i in range(1, n):
#     for j in range(0, i):
#         if arr[j] < arr[i]:
#             dp[i] = max(dp[i], dp[j] + 1)
#
# print(max(dp))

n = int(input())
arr = list(map(int, input().split()))

stack = [arr[0]]

for i in range(1, len(arr)):
    if stack[-1] < arr[i]:
        stack.append(arr[i])
    else:
        start = 0
        end = len(stack)
        while start <= end:
            mid = (start + end) // 2
            if stack[mid] < arr[i]:
                start = mid + 1
            else:
                end = mid - 1
        stack[start] = arr[i]

print(len(stack))
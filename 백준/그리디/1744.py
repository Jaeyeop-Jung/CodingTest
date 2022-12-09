import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()
result = 0
while arr and 1 < arr[-1]:  # 양수인 경우
    pop = arr.pop()
    if arr and 1 < arr[-1]:
        result += arr.pop() * pop
    else:
        result += pop

while arr:  # 1일 경우
    if arr and arr[-1] == 1:
        result += arr.pop()
    else:
        break

arr = deque(arr)
while arr:  # 음수인 경우
    pop = arr.popleft()
    if arr and arr[0] == 0:
        arr.popleft()
    elif arr and arr[0] < 0:
        result += arr.popleft() * pop
    else:
        result += pop



print(result)

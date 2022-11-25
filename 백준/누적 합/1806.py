# TODO 틀림 알고리즘 분류 보지 말고 풀어보기

import math
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

result = math.inf
left, right = 0, 0
total = arr[left]
while left <= right:
    if s <= total:
        result = min(result, right - left + 1)
        total -= arr[left]
        left += 1
    else:
        right += 1
        if len(arr) <= right:
            break
        total += arr[right]

if result != math.inf:
    print(result)
else:
    print(0)



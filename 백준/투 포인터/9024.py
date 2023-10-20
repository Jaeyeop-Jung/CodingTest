import math
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    diff = math.inf
    cnt = 0
    arr.sort()
    left, right = 0, n - 1
    while left < right:
        cur = arr[left] + arr[right]

        # 업데이트
        if abs(k - cur) < diff:
            cnt = 1
            diff = abs(k - cur)
        elif abs(k - cur) == diff:
            cnt += 1

        # 다음
        if cur < k:
            left += 1
        else:
            right -= 1
    print(cnt)

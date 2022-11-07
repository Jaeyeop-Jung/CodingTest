# TODO 틀림 풀 수 있다 잘 생각해봐

import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
onBelt = False
if c in arr:
    onBelt = True
arr *= 2

result = set()
left, right = 0, k - 1
while left < n:
    temp = set(arr[left:right + 1])
    temp.add(c)
    if len(result) < len(temp):
        result = temp

    if right - left < k - 1:
        right += 1
    elif right - left == k - 1:
        left += 1
        right += 1
    else:
        left += 1

if not onBelt:
    result.add(c)

print(len(result))

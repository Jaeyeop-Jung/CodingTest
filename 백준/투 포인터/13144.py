# TODO 틀림 잘 생가해봐 할 수 있다

from collections import deque

n = int(input())
arr = list(map(int, input().split()))

result = 1
left, right = 0, 1
q = deque()
q.append(arr[left])
cur = set()
cur.add(arr[left])
while right < len(arr):
    if arr[right] not in cur:
        result += 1
        q.append(arr[right])
        cur.add(arr[right])
        right += 1
    else:
        while arr[right] in cur:
            cur.remove(q.popleft())
            result += len(q)
        q.append(arr[right])
        cur.add(arr[right])
        result += 1
        right += 1

for term in range(1, len(q)):
    result += term
print(result)
from collections import deque

n, k, = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
cur = deque()
left, right = 0, 0
odd = 0
even = 0
while right < len(arr):
    if arr[right] % 2 == 0:
        even += 1
        cur.append(arr[right])
        right += 1
    else:
        odd += 1
        cur.append(arr[right])
        right += 1
        if k < odd:
            while cur and k < odd:
                pop = cur.popleft()
                if pop % 2 == 0:
                    even -= 1
                else:
                    odd -= 1
    result = max(result, even)

print(result)


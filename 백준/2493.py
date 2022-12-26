from collections import deque

int(input())
arr = list(map(int, input().split()))
arr = [[i, arr[i]] for i in range(len(arr))]

result = [0] * len(arr)
q = deque()
while arr:
    idx, v = arr.pop()
    while q:
        if q[-1][1] <= v:
            resIdx, resV, = q.pop()
            result[resIdx] = idx + 1
            continue
        break
    q.append([idx, v])

print(*result)
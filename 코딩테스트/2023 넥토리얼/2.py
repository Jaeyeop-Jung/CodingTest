from collections import deque

def findMaximumGreatness(arr):
    q = deque(sorted(arr))
    arr.sort()
    res = 0
    while arr:
        other = arr.pop()
        if other < q[-1]:
            q.pop()
            res += 1
        else:
            q.popleft()
    return res


print(findMaximumGreatness(
    [1, 3, 5, 2, 1, 3, 1]
))

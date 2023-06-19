# TODO 틀림

import random


def sol1():
    import sys
    from collections import deque

    input = sys.stdin.readline

    # n, d, k, c = map(int, input().split())
    # arr = [int(input()) for _ in range(n)]
    global arr
    flag = c in arr

    arr += arr
    q = deque()
    cur = set()
    res = 1
    for i in range(n + k):
        if arr[i] in cur:
            while q:
                if q:
                    if c in cur:
                        res = max(res, min(k, len(cur)))
                    else:
                        res = max(res, min(k, len(cur)) + 1)
                pop = q.popleft()
                cur.remove(pop)
                if q:
                    if c in cur:
                        res = max(res, min(k, len(cur)))
                    else:
                        res = max(res, min(k, len(cur)) + 1)
                if pop == arr[i]:
                    break
        cur.add(arr[i])
        q.append(arr[i])

        if c in cur:
            res = max(res, min(k, len(cur)))
        else:
            res = max(res, min(k, len(cur)) + 1)

    return res

def sol2():
    import sys
    input = sys.stdin.readline
    from collections import defaultdict

    global arr
    left = 0
    right = 0
    max_cnt = 0
    eat = defaultdict(int)

    eat[c] += 1

    for right in range(len(arr)):
        eat[arr[right]] += 1

        if right >= k - 1:
            max_cnt = max(max_cnt, len(eat))
            eat[arr[left]] -= 1
            if eat[arr[left]] == 0:
                del eat[arr[left]]
            left += 1

    return max_cnt

for _ in range(100000):
    for n in range(2, 10):
        d = 100
        k = 5
        c = 23
        arr = [random.randrange(1, 100) for _ in range(n)]
        arr += arr
        res1 = sol1()
        res2 = sol2()
        if res1 != res2:
            print(n, d, k, c)
            print(res1, res2)
            print(arr)
            exit()
import sys
from bisect import bisect_left

input = sys.stdin.readline

while True:
    try:
        n = int(input())
        arr = list(map(int, input().split()))

        cur = []
        for i in range(n):
            if not cur or cur[-1] < arr[i]:
                cur.append(arr[i])
            else:
                cur[bisect_left(cur, arr[i])] = arr[i]
        print(len(cur))

    except:
        break
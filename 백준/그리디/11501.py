import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    cur = arr[-1]
    result = 0
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] < cur:
            result += cur - arr[i]
        else:
            cur = arr[i]
    print(result)
import sys

input = sys.stdin.readline

n, l, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0
cover = -1
arr.sort()
for i in range(n):
    start, end = arr[i]
    start = max(start, cover)
    length = end - start

    result += length // l
    length = length % l
    if 0 != length:
        result += 1
        cover = end + l - length

print(result)


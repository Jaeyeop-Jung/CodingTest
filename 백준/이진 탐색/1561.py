import sys

input = sys.stdin.readline

n, m, = map(int, input().split())
arr = list(map(int, input().split()))

if n <= m:
    print(n)
    exit()

n -= m
start, end = 1, 100000000000
while start <= end:
    mid = (start + end) // 2
    temp = sum([mid // i for i in arr])
    if temp < n:
        start = mid + 1
    else:
        end = mid - 1
start -= 1
n -= sum(start // i for i in arr)

start += 1
for i, v in enumerate(arr):
    if start % v == 0:
        n -= 1
        if n == 0:
            print(i + 1)
            exit()
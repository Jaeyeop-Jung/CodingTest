import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

temp = 0
total = [0]
for i in range(n):
    temp += arr[i]
    total.append(temp)

for i in range(m):
    start, end, = map(int, input().split())
    print(total[end] - total[start - 1])



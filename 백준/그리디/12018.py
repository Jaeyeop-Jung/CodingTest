import sys

input = sys.stdin.readline

n, m = map(int, input().split())
classes_info = []
points = []
for i in range(n):
    p, l = map(int, input().split())
    temp = list(map(int, input().split()))

    temp.sort(reverse=True)
    if p + 1 <= l:
        points.append(1)
    else:
        points.append(temp[l - 1])

points.sort()
result = 0
for i in range(len(points)):
    if points[i] <= m:
        m -= points[i]
        result += 1
    else:
        break

print(result)
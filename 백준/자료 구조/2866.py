import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input().strip() for _ in range(n)]

newArr = []
for c in range(m):
    temp = ''
    for r in range(n):
        temp += arr[r][c]
    newArr.append(temp)

res = 0
for start in range(1, n):
    cur = set()
    for r in range(m):
        temp = newArr[r][start:]
        if temp in cur:
            print(res)
            exit()
        cur.add(temp)
    res += 1
print(res)
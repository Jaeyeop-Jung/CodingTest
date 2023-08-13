import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
reverseDic = {}
for i in range(m):
    cur = input().strip()
    dic[cur] = i
    reverseDic[i] = cur

cnt = 0
idx = 0
while idx < m and cnt < n:
    cur = reverseDic[idx]
    if dic[cur] == idx:
        print(cur)
        cnt += 1
    idx += 1
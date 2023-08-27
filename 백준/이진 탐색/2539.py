import sys

input = sys.stdin.readline

n, m, = map(int, input().split())
paperCnt = int(input())
k = int(input())
arr = []
for _ in range(k):
    r, c = map(int, input().split())
    arr.append((r, c))


def canTape(size):
    visited = [False] * k
    cnt = 0
    for i in range(k):
        if visited[i]:
            continue
        cnt += 1
        r, c = arr[i]
        for j in range(i + 1, k):
            nextR, nextC, = arr[j]
            if nextC < c + size:
                visited[j] = True
            else:
                break
    return cnt <= paperCnt


arr.sort(key=lambda x: x[1])
start, end = min(max([i[0] for i in arr]), max([i[1] for i in arr])), n
res = end
while start <= end:
    mid = (start + end) // 2
    if canTape(mid):
        res = mid
        end = mid - 1
    else:
        start = mid + 1

print(res)
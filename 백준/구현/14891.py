from collections import deque

left, right = 6, 2

arr = [deque(list(map(int, list(input())))) for _ in range(4)]
n = int(input())
for _ in range(n):
    num, d, = map(int, input().split())
    visited = [0] * 4
    visited[num - 1] = d
    q = deque()
    q.append([num - 1, d])
    while q:
        target, d, = q.popleft()
        if 1 <= target and arr[target - 1][right] != arr[target][left] and visited[target - 1] == 0:
            q.append([target - 1, -d])
            visited[target - 1] = -d
        if target <= 2 and arr[target][right] != arr[target + 1][left] and visited[target + 1] == 0:
            q.append([target + 1, -d])
            visited[target + 1] = -d
    for i in range(4):
        arr[i].rotate(visited[i])

result = 0
for i in range(4):
    if arr[i][0] == 1:
        result += 2 ** i
print(result)

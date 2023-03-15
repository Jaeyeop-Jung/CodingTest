import sys

input = sys.stdin.readline

n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0

def isPossible(arr):
    cur = arr[0]
    i = 0
    visited = [False] * n
    while i < n:
        if arr[i] == cur:
            i += 1
            continue
        elif arr[i] == cur - 1:
            if n < i + l:
                break
            for j in range(i, i + l):
                if arr[j] != arr[i] or visited[j]:
                    break
            else:
                for j in range(i, i + l):
                    visited[j] = True
                i = i + l
                cur -= 1
                continue
            break
        elif arr[i] == cur + 1:
            if i - l < 0:
                break
            for j in range(i - l, i):
                if arr[j] != cur or visited[j]:
                    break
            else:
                for j in range(i - l, i):
                    visited[j] = True
                i += 1
                cur += 1
                continue
            break
        else:
            break
    else:
        return True
    return False

# 가로
for r in range(n):
    if isPossible(arr[r]):
        result += 1
# 세로
for c in range(n):
    temp = [arr[i][c] for i in range(n)]
    if isPossible(temp):
        result += 1

print(result)
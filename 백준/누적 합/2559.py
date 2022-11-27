import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = sum(arr[:m])
temp = result
idx = 0
for i in range(m, len(arr)):
    temp += arr[i]
    temp -= arr[idx]
    result = max(result, temp)
    idx += 1

print(result)


n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while start <= end:
    middle = (start + end) // 2
    total = sum([i - middle for i in arr if i - middle >= 0])
    if total == m:
        result = middle
        break
    elif total < m:
        end = middle - 1
    else:
        start = middle + 1
        result = middle

print(result)
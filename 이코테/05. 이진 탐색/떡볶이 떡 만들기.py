
n, m = map(int, input().split())
data = list(map(int, input().split()))


# for i in range(max(data), min(data) - 1, -1):
#     count = sum([j - i for j in data if j - i >= 0])
#     if count >= m:
#         print(i)
#         break

result = 0
start = 0
end = max(data)
while start <= end:
    middle = (start + end) // 2
    total = sum([i - middle for i in data])

    if total < m:
        end = middle - 1
    else:
        result = middle
        start = middle + 1
print(result)
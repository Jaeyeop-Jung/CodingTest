
n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    arr[i] = [i + 1, arr[i]]

arr.sort(key=lambda x: x[1])
result = []
for idx, left in arr:
    if not result:
        result.append(idx)
    else:
        cnt = 0
        for i in range(len(result)):
            if idx < result[i]:
                cnt += 1
            if left < cnt:
                result.insert(i, idx)
                break
        else:
            result.append(idx)

print(*result)

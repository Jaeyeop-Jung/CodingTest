
n = int(input())
arr = list(map(int, input().split()))

def getFunc(x1, y1, x2, y2):
    cal = (y2 - y1) / (x2 - x1)
    return cal, y1 - cal * x1

result = 0
for cur in range(len(arr)):
    temp = 0
    for i in range(cur):
        cal, const, = getFunc(i + 1, arr[i], cur + 1, arr[cur])
        for j in range(i + 1, cur):
            if cal * (j + 1) + const <= arr[j]:
                break
        else:
            temp += 1
    for i in range(cur + 1, n):
        cal, const, = getFunc(cur + 1, arr[cur], i + 1, arr[i])
        for j in range(cur + 1, i):
            if cal * (j + 1) + const <= arr[j]:
                break
        else:
            temp += 1
    result = max(result, temp)

print(result)
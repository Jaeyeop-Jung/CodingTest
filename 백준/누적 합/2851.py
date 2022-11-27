import sys
input = sys.stdin.readline

arr = []
for i in range(10):
    arr.append(int(input()))

temp = 0
result = 100 * 10
for i in range(len(arr)):
    temp += arr[i]
    diff = abs(100 - temp)
    diffRes = abs(100 - result)
    if diff == diffRes:
        result = max(result, temp)
    elif diff < diffRes:
        result = temp

print(result)
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1
result = arr[left] + arr[right]
resultArr = [arr[left], arr[right]]
while left < right:
    temp = arr[left] + arr[right]
    if abs(temp) < abs(result):
        resultArr = [arr[left], arr[right]]
        result = temp
        if temp == 0:
            break

    if temp < 0:
        left += 1
    else:
        right -= 1
print(resultArr[0], resultArr[1])
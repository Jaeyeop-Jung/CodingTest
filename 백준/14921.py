import math

n = int(input())
arr = list(map(int, input().split()))

left, right = 0, n - 1
res = math.inf
while left < right:
    suma = arr[left] + arr[right]
    if abs(suma) < abs(res):
        res = suma

    if suma == 0:
        print(0)
        exit()
    elif suma < 0:
        left += 1
    else:
        right -= 1

print(res)
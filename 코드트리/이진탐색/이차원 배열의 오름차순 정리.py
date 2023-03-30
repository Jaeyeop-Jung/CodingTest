# TODO 틀림

n = int(input())
target = int(input())

left, right = 1, n ** 2
while left <= right:
    mid = (left + right) // 2
    num = 0
    for i in range(1, n + 1):
        num += min(n, mid // i)
    if target <= num:
        right = mid - 1
    else:
        left = mid + 1

print(left)



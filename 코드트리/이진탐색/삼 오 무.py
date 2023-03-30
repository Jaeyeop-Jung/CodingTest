# TODO 틀림

n = int(input())
left = 1
right = 10 ** 10
while left <= right:
    mid = (left + right) // 2
    num = mid - mid // 3 - mid // 5 + mid // 15
    if num < n:
        left = mid + 1
    else:
        right = mid - 1
print(left)

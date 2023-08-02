import math

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
diff = math.inf
res = []
for i in range(n - 2):
    left = i + 1
    right = n - 1
    while left < right:
        tempTotal = arr[i] + arr[left] + arr[right]
        tempDiff = abs(tempTotal)
        if tempDiff == 0:
            print(*sorted([arr[i], arr[left], arr[right]]))
            exit()
        else:
            if tempDiff < diff:
                res = sorted([arr[i], arr[left], arr[right]])
                diff = tempDiff
            if tempTotal > 0:
                right -= 1
            else:
                left += 1

print(*res)
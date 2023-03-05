# TODO 틀림 할 수 있다 잘 생각해봐

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
result = 0
for i in range(len(arr)):
    l, r = i + 1, n - 1
    while l < r:
        total = arr[i] + arr[l] + arr[r]
        if total == 0:
            if arr[l] == arr[r]:
                result += r - l
            else:
                target = arr[r]
                tempR = r
                while arr[tempR] == target:
                    tempR -= 1
                    result += 1
            l += 1
        elif total < 0:
            l += 1
        else:
            r -= 1

print(result)
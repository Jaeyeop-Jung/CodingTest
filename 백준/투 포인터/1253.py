# TODO 틀림

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0
for separator in range(len(arr)):
    temp = arr[:separator] + arr[separator + 1:]
    start = 0
    end = len(temp) - 1
    while start < end:
        if temp[start] + temp[end] == arr[separator]:
            result += 1
            break
        elif temp[start] + temp[end] < arr[separator]:
            start += 1
        else:
            end -= 1

print(result)



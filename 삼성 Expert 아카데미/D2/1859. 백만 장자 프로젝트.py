# TODO 틀림

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    result = 0
    max_value = n - 1
    for i in range(len(arr) - 1, -1, -1):
        if arr[max_value] < arr[i]:
            result += sum([arr[max_value] - arr[j] for j in range(i+1, max_value)])
            max_value = i
    result += sum([arr[max_value] - arr[i] for i in range(max_value) if 0 < arr[max_value] - arr[i]])

    print('#' + str(test_case) + ' ' + str(result))

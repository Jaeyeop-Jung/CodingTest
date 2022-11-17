
T = 10
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    result = 0
    for i in range(2, len(arr) - 2):
        sun = min(arr[i] - max(arr[i - 1], arr[i - 2]), arr[i] - max(arr[i + 1], arr[i + 2]))
        if 0 < sun:
            result += sun

    print('#' + str(test_case) + ' ' + str(result))

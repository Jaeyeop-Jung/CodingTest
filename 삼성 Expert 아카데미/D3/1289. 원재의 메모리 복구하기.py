
T = int(input())
for test_case in range(1, T + 1):
    target = list(input())

    result = 0
    arr = ['0'] * len(target)
    for i in range(len(target)):
        if target[i] != arr[i]:
            arr = arr[:i] + list(target[i] * (len(arr) - i))
            result += 1

    print('#' + str(test_case) + ' ' + str(result))
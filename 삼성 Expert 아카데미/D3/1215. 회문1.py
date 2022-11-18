# TODO 틀림 펠린드롬 이해 외우자

def isPailn(str):
    return str == str[::-1]

T = 10
for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    for i in range(8):
        arr.append(list(input()))

    result = []
    for i in range(8):
        for j in range(8 - n + 1):
            join = ''.join(arr[i][j:j + n])
            if isPailn(join):
                result.append(join)
    for i in range(8 - n + 1):
        for j in range(8):
            join = ''.join([arr[r][j] for r in range(i, i + n)])
            if isPailn(join):
                result.append(join)

    print('#' + str(test_case) + ' ' + str(len(result)))
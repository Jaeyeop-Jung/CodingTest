
import sys
sys.stdin = open("C:/Users/user/Downloads/1216.txt", "r")

T = 10
for test_case in range(1, T + 1):
    _ = input()
    arr = []
    for _ in range(100):
        arr.append(list(input()))

    result = 1
    flag = False
    for length in range(100, 1, -1):
        for r in range(100):
            for c in range(101 - length):
                if arr[r][c:c+length] == arr[r][c:c+length][::-1]:
                    result = max(result, length)
                    flag = True
                    break
        if flag:
            break

    flag = False
    for length in range(100, 1, -1):
        for c in range(100):
            for r in range(101 - length):
                temp = [arr[row][c] for row in range(r, r + length)]
                if temp == temp[::-1]:
                    result = max(result, length)
                    flag = True
                    break
        if flag:
            break

    print('#' + str(test_case) + ' ' + str(result))



# import sys
#
# sys.stdin = open("/Users/jeongjaeyeob/Downloads/1220.txt", "r")

def getDeadlock(arr):
    flag = False
    count = 0
    for i in arr:
        if i == 1:
            flag = True
        if flag and i == 2:
            flag = False
            count += 1
    return count

T = 10
for test_case in range(1, T + 1):
    n = int(input())
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))

    result = 0
    for c in range(n):
        result += getDeadlock([board[r][c] for r in range(n)])

    print('#' + str(test_case) + ' ' + str(result))

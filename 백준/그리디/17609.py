# TODO 틀림 잘 생각해봐라 맞을 수 있다

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

n = int(input())
arr = [list(input().strip()) for _ in range(n)]

def isAva(arr, left, right):
    while left < right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def isAvailable(arr, left, right):
    while left < right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        else:
            length = (len(arr) - 1) // 2
            res = isAva(arr, left + 1, right) or isAva(arr, left, right - 1)
            if not res:
                print(2)
            else:
                print(1)
            return
    print(0)
    return

for i in range(n):
    string = arr[i]
    left, right = 0, len(string) - 1
    isAvailable(string, left, right)


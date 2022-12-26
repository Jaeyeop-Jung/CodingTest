# TODO 틀림 아이디어가 생각보다 어려움

import sys
input = sys.stdin.readline

n, m, = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in range(len(arr)):
    temp = 0
    for j in range(i, len(arr)):
        temp += arr[j]
        if temp % m == 0:
            result += 1

print(result)

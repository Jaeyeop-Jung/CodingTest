# TODO 틀림 https://jaeyoon-95.tistory.com/168

import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

firstSumList = {}
for i in range(n):
    for j in range(n):
        tempSum = arr[i][0] + arr[j][1]
        firstSumList[tempSum] = firstSumList.get(tempSum, 0) + 1

result = 0
for i in range(n):
    for j in range(n):
        temp = -(arr[i][2] + arr[j][3])
        if temp in firstSumList:
            result += firstSumList[temp]

print(result)

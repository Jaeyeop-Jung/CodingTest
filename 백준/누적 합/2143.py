# TODO 틀림

import sys
input = sys.stdin.readline

target = int(input())
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

dic1 = {}
for i in range(len(arr1)):
    for j in range(i + 1, len(arr1) + 1):
        dic1[sum(arr1[i:j])] = dic1.get(sum(arr1[i:j]), 0) + 1
dic2 = {}
for i in range(len(arr2)):
    for j in range(i + 1, len(arr2) + 1):
        dic2[sum(arr2[i:j])] = dic2.get(sum(arr2[i:j]), 0) + 1

result = 0
for d1 in dic1:
    if target - d1 in dic2:
        result += dic1[d1] * dic2[target - d1]

print(result)
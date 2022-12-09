import sys
import math
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

result = 0
# if b < c:
#     for num in arr:
#         result += round(num / c)
# else:
for num in arr:
    num -= b
    result += 1
    if 0 < num:
        result += math.ceil(num / c)

print(result)
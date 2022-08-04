import sys

input = sys.stdin.readline

input = int(input())
list = [500, 100, 50, 10]
result = 0
for i in list:
    result += input // i
    input %= i

print(result)
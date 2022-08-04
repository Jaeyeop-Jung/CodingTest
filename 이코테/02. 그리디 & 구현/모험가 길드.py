import sys

input = sys.stdin.readline

n = int(input())
list = list(map(int, input().split()))

list.sort()
result = 0
cnt = 0
necessary = 0
for i in range(len(list)):
    if necessary == 0 or necessary < list[i]:
        necessary = list[i]
    cnt += 1
    if necessary == cnt:
        result += 1
        cnt = 0
        necessary = 0

print(result)
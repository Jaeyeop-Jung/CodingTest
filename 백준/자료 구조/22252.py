import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

n = int(input())
dic = defaultdict(list)

res = 0
for _ in range(n):
    arr = list(input().split())
    if arr[0] == '1':
        for i in range(int(arr[2])):
            heapq.heappush(dic[arr[1]], -int(arr[i + 3]))
    else:
        for _ in range(int(arr[2])):
            if not dic[arr[1]]:
                break
            res += -heapq.heappop(dic[arr[1]])
print(res)


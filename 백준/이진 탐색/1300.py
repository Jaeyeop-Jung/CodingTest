# TODO 틀림 https://slowsure.tistory.com/134

# n = int(input())
# k = int(input())
#
# row = (k - 1) // n
# column = (k - 1) % n
#
# if column == 0:
#     print(row * n)
# else:
#     print(row * column * n)

import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

start, end = 0, k
# k번째 수는 k보다 클 수 없음

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in range(1, n + 1):
        cnt += min(mid // i, n)

    if cnt >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
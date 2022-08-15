# TODO 틀림 https://hongcoding.tistory.com/5

# import sys
#
# input = sys.stdin.readline
#
# n, h = map(int, input().split())
# arr = [int(input()) for i in range(n)]
#
# start = 1
# end = h
# hitList = []
# hit = n
# result = 0
#
# for i in range(h):
#     cnt = 0
#     for j in range(len(arr)):
#         if j % 2 == 0:
#             if arr[j] >= i:
#                 cnt += 1
#         else:
#             if h - i + 1 <= arr[j]:
#                 cnt += 1
#
#     if cnt <= hit:
#         result = i
#         hit = cnt
#         end = i - 1
#         hitList.append(hit)
#     else:
#         start = i + 1
#         hitList.append(cnt)
#
#
# while start <= end:
#     mid = (start + end) // 2
#     cnt = 0
#     for i in range(len(arr)):
#         if i % 2 == 0:
#             if arr[i] >= mid:
#                 cnt += 1
#         else:
#             if h - mid + 1 <= arr[i]:
#                 cnt += 1
#
#     if cnt <= hit:
#         result = mid
#         hit = cnt
#         end = mid - 1
#         hitList.append(hit)
#     else:
#         start = mid + 1
#         hitList.append(cnt)
#
# print(hit, hitList.count(hit))

from bisect import bisect_left

n, h = map(int, input().split())

down = []
up = []
for i in range(n):
    if i % 2 == 0:
        down.append(int(input()))
    else:
        up.append(int(input()))

down.sort()
up.sort()

min_count = n
range_count = 0

for i in range(1, h + 1):
    down_count = len(down) - bisect_left(down, i - 0.5)
    top_count = len(up) - bisect_left(up, h - i + 0.5)

    if min_count == down_count + top_count:
        range_count += 1
    elif min_count > down_count + top_count: # 현재 범위가 새로운 최소 값이면
        range_count = 1
        min_count = down_count + top_count

print(min_count, range_count)
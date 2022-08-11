# TODO 틀림 https://dailymapins.tistory.com/232?category=1017255

import sys

input = sys.stdin.readline

t = int(input())
# for _ in range(t):
#     n = int(input())
#     data = []
#     for i in range(n):
#         a, b, = map(int, input().split())
#         data.append([a, b, False])
#     data.sort(key=lambda x: x[0], reverse=True)
#     for i in range(len(data) - 1):
#         for j in range(i, len(data)):
#             if data[i][2] is True or data[i][1] == 1:
#                 break
#             if data[i][1] > data[j][1]:
#                 data[i][2] = True
#     data.sort(key=lambda x: x[1], reverse=True)
#     for i in range(len(data) - 1):
#         for j in range(i, len(data)):
#             if data[i][2] is True or data[i][0] == 1:
#                 break
#             if data[i][0] > data[j][0]:
#                 data[i][2] = True
#     result = 0
#     for i in data:
#         if i[2] is False:
#             result += 1
#     print(result)

for _ in range(t):
    n = int(input())
    data = []
    for i in range(n):
        a, b, = map(int, input().split())
        data.append([a, b])
    data.sort(key=lambda x: x[0])
    result = 1
    hiredScore = data[0][1]
    for i in range(1, n):
        if data[i][1] < hiredScore:
            result += 1
            hiredScore = data[i][1]
    print(result)
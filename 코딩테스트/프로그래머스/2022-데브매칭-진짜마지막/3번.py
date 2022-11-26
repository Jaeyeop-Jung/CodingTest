# import heapq
# import math
#
#
# def dijkstra(subway, locate, start, end):
#     h = []
#     heapq.heappush(h, [0, locate, subway[locate].index(start)])
#     distance = [math.inf] * 1000001
#     distance[start] = 0
#     while h:
#         cnt, curLocate, curIdx, = heapq.heappop(h)
#         if distance[subway[curLocate][curIdx]] < cnt:
#             continue
#         for i in range(len(subway[curLocate])):
#             distance[subway[curLocate][i]] = cnt
#
#
# trans = {}
# def solution(subway, start, end):
#     for i in range(len(subway)):
#         subway[i] = list(map(int, subway[i].split(' ')))
#
#     for i in range(len(subway)):
#         if start in subway[i]:
#             if end in subway[i]:
#                 return 0
#             dijkstra(subway, i, start, end)
import math


def solution(subway, start, end):
    maxStation = 0
    for i in range(len(subway)):
        subway[i] = sorted(list(map(int, subway[i].split(' '))))
        maxStation = max(maxStation, max(subway[i]))
    subway.sort(key=lambda x: len(x))

    distance = [math.inf] * (maxStation + 1)
    distance[start] = 0
    for i in range(len(subway)):
        if start in subway[i]:
            for j in subway[i]:
                distance[j] = 0

    for i in range(len(distance)):
        if distance[i] == 0:
            for j in range(len(subway)):
                if i in subway[j]:
                    for k in subway[j]:
                        distance[k] = min(distance[k], distance[i] + 1)
    return distance[end]


print(solution(["1 2 3 4 5 6 7 8", "2 11", "0 11 10", "3 17 19 12 13 9 14 15 10", "20 2 21"], 1, 9))

# import heapq
#
# def solution(food_times, k):
#     h = []
#     for i, v in enumerate(food_times):
#         heapq.heappush(h, [i, v])
#
#     tempH = []
#     for _ in range(k):
#         if not h:
#             if not tempH:
#                 return -1
#             h = tempH
#             tempH = []
#             i, v, = heapq.heappop(h)
#             v -= 1
#             if 0 < v:
#                 heapq.heappush(tempH, [i, v])
#         else:
#             i, v, = heapq.heappop(h)
#             v -= 1
#             if 0 < v:
#                 heapq.heappush(tempH, [i, v])
#
#     if h:
#         return heapq.heappop(h)[0] + 1
#     else:
#         return heapq.heappop(tempH)[0] + 1

from collections import deque
def solution(food_times, k):
    food_times = [[i, v] for i, v in enumerate(food_times)]
    food_times.sort(key=lambda x: (x[1], x[0]))

    food_times = deque(food_times)
    cnt = 0
    n = len(food_times)
    cur = 0
    while food_times:
        i, v = food_times.popleft()
        if k < cnt + n * (v - cur):
            food_times.appendleft([i, v])
            break
        popCnt = 1
        while food_times and food_times[0][1] == v:
            food_times.popleft()
            popCnt += 1
        cnt += n * (v - cur)
        n -= popCnt
        cur = v

    if not food_times:
        return -1
    else:
        l = sorted([i for i, _ in food_times])
        return l[(k - cnt) % len(l)] + 1


# print(solution([4, 2, 3, 1, 4, 2], 12))
# print(solution([3, 1, 2], 5))
# print(solution([1, 1, 1, 1, 1, 1], 3))
# print(solution([1, 101], 100))
print(solution([1, 1, 1, 1], 4))
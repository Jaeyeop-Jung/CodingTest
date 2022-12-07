# TODO 틀림 깊게 생각 해봐

# import math
#
# def solution(land, P, Q):
#     start = min(map(min, land))
#     end = max(map(max, land))
#     result = math.inf
#     # while start <= end:
#     #     mid = (start + end) // 2
#     #     cost = 0
#     #     for r in range(len(land)):
#     #         for c in range(len(land[r])):
#     #             if land[r][c] == mid:
#     #                 continue
#     #             elif land[r][c] < mid:
#     #                 cost += abs(mid - land[r][c]) * P
#     #             else:
#     #                 cost += abs(mid - land[r][c]) * Q
#     #     if cost < result:
#     #         if P < Q:
#     #             start = mid + 1
#     #         else:
#     #             end = mid - 1
#     #     else:
#     #         return result
#     #     result = min(result, cost)
#
#     while start <= end:
#         mid = (start + end) // 2
#         costUp = 0
#         costDown = 0
#         for r in range(len(land)):
#             for c in range(len(land[r])):
#                 if land[r][c] == mid:
#                     continue
#                 elif land[r][c] < mid:
#                     costUp += abs(mid - land[r][c]) * P
#                 else:
#                     costDown += abs(mid - land[r][c]) * Q
#         if costUp + costDown < result:
#             result = costUp + costDown
#         else:
#             break
#         if costUp < costDown:
#             start = mid + 1
#         else:
#             end = mid - 1
#
#     return result

import math
def solution(land, P, Q):
    arr = [land[r][c] for r in range(len(land)) for c in range(len(land[r]))]
    arr.sort()

    cost = (sum(arr) - arr[0] * len(arr)) * Q
    result = cost
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            continue
        cost = cost + ((arr[i] - arr[i-1]) * P * i) - ((arr[i] - arr[i-1]) * (len(arr) - i) * Q)
        result = min(result, cost)

    return result

print(solution([[1, 2], [2, 3]], 3, 2))
print(solution([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]], 5, 3))
# print(solution([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]], 5, 3))

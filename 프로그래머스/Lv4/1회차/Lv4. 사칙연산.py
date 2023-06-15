# TODO 틀림 다음엔 맞을 수 있다

import math

def dfs(arr, l, r):
    if l == r:
        return int(arr[l]), int(arr[l])
    if (l, r) in minDp:
        return minDp[(l, r)], maxDp[(l, r)]

    minDp[(l, r)] = math.inf
    maxDp[(l, r)] = -math.inf
    for sep in range(l, r, 2):
        preMin, preMax = dfs(arr, l, sep)
        postMin, postMax = dfs(arr, sep + 2, r)

        if arr[sep + 1] == '+':
            minDp[(l, r)] = min(
                minDp[(l, r)],
                preMin + postMin,
                preMin + postMax,
                preMax + postMin,
                preMax + postMax
            )
            maxDp[(l, r)] = max(
                maxDp[(l, r)],
                preMin + postMin,
                preMin + postMax,
                preMax + postMin,
                preMax + postMax
            )
        else:
            minDp[(l, r)] = min(
                minDp[(l, r)],
                preMin - postMin,
                preMin - postMax,
                preMax - postMin,
                preMax - postMax
            )
            maxDp[(l, r)] = max(
                maxDp[(l, r)],
                preMin - postMin,
                preMin - postMax,
                preMax - postMin,
                preMax - postMax
            )

    return minDp[(l, r)], maxDp[(l, r)]

def solution(arr):
    global minDp, maxDp
    n = len(arr)
    minDp = {}
    maxDp = {}
    return dfs(arr, 0, n - 1)[1]

# import math
# def solution(arr):
#     n = len(arr)
#     minDp = [[math.inf] * n for _ in range(n)]
#     maxDp = [[-math.inf] * n for _ in range(n)]
#
#     for i in range(0, n, 2):
#         minDp[i][i] = int(arr[i])
#         maxDp[i][i] = int(arr[i])
#     for i in range(0, n - 2, 2):
#         minDp[i][i + 2] = eval(''.join(arr[i:i+3]))
#         maxDp[i][i + 2] = eval(''.join(arr[i:i + 3]))
#
#     for cnt in range(4, n, 2):
#         for left in range(0, n, 2):
#             right = left + cnt
#             if n <= right:
#                 continue
#             for sep in range(left, right, 2):
#                 if arr[sep + 1] == '+':
#                     minDp[left][right] = min(
#                         minDp[left][right],
#                         minDp[left][sep] + minDp[sep + 2][right],
#                         minDp[left][sep] + maxDp[sep + 2][right],
#                         maxDp[left][sep] + minDp[sep + 2][right],
#                         maxDp[left][sep] + maxDp[sep + 2][right]
#                     )
#                     maxDp[left][right] = max(
#                         maxDp[left][right],
#                         minDp[left][sep] + minDp[sep + 2][right],
#                         minDp[left][sep] + maxDp[sep + 2][right],
#                         maxDp[left][sep] + minDp[sep + 2][right],
#                         maxDp[left][sep] + maxDp[sep + 2][right]
#                     )
#                 else:
#                     minDp[left][right] = min(
#                         minDp[left][right],
#                         minDp[left][sep] - minDp[sep + 2][right],
#                         minDp[left][sep] - maxDp[sep + 2][right],
#                         maxDp[left][sep] - minDp[sep + 2][right],
#                         maxDp[left][sep] - maxDp[sep + 2][right]
#                     )
#                     maxDp[left][right] = max(
#                         maxDp[left][right],
#                         minDp[left][sep] - minDp[sep + 2][right],
#                         minDp[left][sep] - maxDp[sep + 2][right],
#                         maxDp[left][sep] - minDp[sep + 2][right],
#                         maxDp[left][sep] - maxDp[sep + 2][right]
#                     )
#     return maxDp[0][n - 1]

print(solution(["1", "-", "3", "+", "5", "-", "8"]))
print(solution(["1", "-", "3", "+", "5"]))
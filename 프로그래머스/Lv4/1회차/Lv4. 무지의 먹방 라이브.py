#
# def solution(food_times, k):
#     rotate = k // len(food_times)
#     rest = k % len(food_times)
#
#     for i in range(len(food_times)):
#         if food_times[i] - rotate < 0:
#             rest -= food_times[i] - rotate
#             food_times[i] = 0
#         else:
#             food_times[i] -= rotate
#
#     result = 0
#     cnt = 0
#     while 0 < rest:
#         if cnt == len(food_times):
#             break
#         if food_times[result] == 0:
#             result += 1
#             result %= len(food_times)
#             cnt += 1
#             continue
#         food_times[result] -= 1
#         result += 1
#         result %= len(food_times)
#         rest -= 1
#         cnt = 0
#
#     for i in range(result, len(food_times)):
#         if food_times[i] != 0:
#             return i + 1
#     for i in range(result):
#         if food_times[i] != 0:
#             return i + 1
#     return -1

def solution(food_times, k):
    foods = [[i + 1, food_times[i]] for i in range(len(food_times))]
    foods.sort(key=lambda x: x[1])

    bp = 0
    n = len(foods)
    pretime = 0
    for i in range(n):
        cnt = (foods[i][1] - pretime) * n
        if cnt == 0:
            pretime = foods[i][1]
            n -= 1
            continue
        if k - cnt < 0:
            bp = i
            break
        k -= cnt
        n -= 1
        pretime = foods[i][1]
    else:
        return -1

    foods = foods[bp:]
    foods.sort(key=lambda x: x[0])

    return foods[k % len(foods)][0]


print(solution([1,1,1,1], 4))
# print(solution([2, 2, 7, 3], 12))
# print(solution([3, 1, 2], 10))
# print(solution([15], 10))
# print(solution([100000000] * 200000, 10 ** 13))

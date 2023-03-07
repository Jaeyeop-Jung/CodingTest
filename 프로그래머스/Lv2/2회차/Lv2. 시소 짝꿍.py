# TODO 틀림 다음엔 무조건 맞아라 좀..

from collections import defaultdict
from collections import Counter
import math

# def solution(weights):
#     weights.sort()
#
#     dic = defaultdict(set)
#     for i in range(len(weights)):
#         for j in [2, 3, 4]:
#             dic[weights[i] * j].add(i)
#
#     result = set()
#     for i, weight in enumerate(weights):
#         for j in [2, 3, 4]:
#             for idx in dic[weight * j]:
#                 if i != idx:
#                     result.add((i, idx))
#
#     return len(result) // 2

# def solution(weights):
#     weights.sort()
#     dic = defaultdict(int)
#     for i in set(weights):
#         for j in [2, 3, 4]:
#             dic[i * j] += 1
#
#     result = 0
#     for weight in set(weights):
#         for j in [2, 3, 4]:
#             if 0 < dic[weight * j]:
#                 result += math.comb(dic[weight * j], 2)
#                 dic[weight * j] = 0
#
#     counter = Counter(weights)
#     for key in counter:
#         if 2 <= counter[key]:
#             result += math.comb(counter[key], 2)
#
#     return result

def solution(weights):
    count = 0
    positions = [(2, 3), (2, 4), (3, 4), (4, 3), (4, 2), (3, 2)]

    # 초기화
    weight_map = {}
    for weight in weights:
        weight_map.setdefault(weight, 0)
        weight_map[weight] += 1

    for my_weight in weight_map:
        # 본인이랑 같은 무게의 친구가 있을 경우
        if weight_map[my_weight] > 1:
            count += weight_map[my_weight] * (weight_map[my_weight] - 1) // 2
        # 본인의 몸무게로 평형을 맞출 수 있는 경우
        for (my_position, friend_position) in positions:
            expected_friend_weight = my_weight * my_position / friend_position
            if (expected_friend_weight in weight_map):
                count += weight_map[my_weight] * weight_map[expected_friend_weight]
        # 이미 계산을 끝낸 몸무게는 중복 계산이 되지 않도록 제거해준다
        weight_map[my_weight] = 0

    return count

print(solution([100, 180, 360, 100, 270]))

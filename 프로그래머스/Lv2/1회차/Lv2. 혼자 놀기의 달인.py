from itertools import combinations

# def solution(cards):
#     result = 0
#     for pick in combinations(cards, 1):
#         temp = cards[:]
#         group1 = []
#         pick = pick[0]
#         while True:
#             if temp[pick - 1] == -1:
#                 break
#             group1.append(pick)
#             newPick = temp[pick - 1]
#             temp[pick - 1] = -1
#             pick = newPick
#
#         for i in combinations([i for i in temp if i != -1], 1):
#             temp2 = temp[:]
#             group2 = []
#             pick2 = i[0]
#             while True:
#                 if temp2[pick2 - 1] == -1:
#                     break
#                 group2.append(pick2)
#                 newPick = temp2[pick2 - 1]
#                 temp2[pick2 - 1] = -1
#                 pick2 = newPick
#
#             result = max(result, len(group1) * len(group2))
#
#     return result

def solution(cards):
    answer = []
    for i in range(len(cards)):
        tmp = []
        while cards[i] not in tmp:
            tmp.append(cards[i])
            i = cards[i] - 1
        answer.append([] if sorted(tmp) in answer else sorted(tmp))
    answer.sort(key=len)

    return len(answer[-1]) * len(answer[-2])

print(solution([8,6,3,7,2,5,1,4]))

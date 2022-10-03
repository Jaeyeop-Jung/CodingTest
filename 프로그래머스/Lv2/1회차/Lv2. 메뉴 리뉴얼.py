from itertools import combinations

def solution(orders, course):
    answer = []
    hash_map = {}
    for i in course:
        for j in orders:
            for k in combinations(j, i):
                k = sorted(k)
                k = tuple(k)
                if k in hash_map:
                    hash_map[k] += 1
                else:
                    hash_map[k] = 1
    for i in course:
        data = []
        for j in hash_map:
            if len(j) == i:
                data.append([j, hash_map[j]])
        if data:
            m = max(data, key=lambda x: x[1])
            maxMenu = []
            for i in data:
                if i[1] == m[1]:
                    maxMenu.append(i)
            answer.append(maxMenu)

    realAnswer = []
    for i in answer:
        if len(i) == 1:
            if i[0][1] >= 2:
                realAnswer.append("".join(i[0][0]))
        else:
            for j in range(len(i)):
                if i[j][1] >= 2:
                    realAnswer.append("".join(i[j][0]))
    realAnswer.sort()
    return realAnswer

# from itertools import combinations
# from collections import Counter
# def solution(orders, course):
#     answer = []
#     for k in course:
#         candidates = []
#         for menu_li in orders:
#             for li in combinations(menu_li, k):
#                 res = ''.join(sorted(li))
#                 candidates.append(res)
#         sorted_candidates = Counter(candidates).most_common()
#         answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]
#     return sorted(answer)

solution(["XYZ", "XWY", "WXA"], [2,3,4])
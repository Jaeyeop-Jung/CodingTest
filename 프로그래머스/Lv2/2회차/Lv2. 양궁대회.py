# from itertools import combinations_with_replacement
#
# def solution(n, info):
#     info.reverse()
#
#     result = []
#     # 중복조합으로 뽑고, 점수 비교해서 제일 큰거면 result에 넣고
#     for pick in combinations_with_replacement([i for i in range(11)], n):
#         temp = [0] * 11
#         for i in pick:
#             temp[i] += 1
#
#         apeachScore = 0
#         ryonScore = 0
#         for i in range(len(temp)):
#             if info[i] == temp[i] == 0:
#                 continue
#             if info[i] < temp[i]:
#                 ryonScore += i
#             else:
#                 apeachScore += i
#
#         if apeachScore < ryonScore:
#             result.append([ryonScore - apeachScore, temp])
#
#     # result에서 낮은거 많이 쏠수록 소트해서 return
#     if not result:
#         return [-1]
#
#     result.sort(key=lambda x: (-x[0], -x[1][0], -x[1][1], -x[1][2], -x[1][3], -x[1][4], -x[1][5], -x[1][6], -x[1][7], -x[1][8], -x[1][9], -x[1][10]))
#
#     return list(reversed(result[0][1]))
import operator

answer, result = 0, []
def dfs(info, score, n, index):
    if index == 11 and n:
        return
    if n == 0:
        apeachScore = 0
        ryonScore = 0
        for i in range(len(score)):
            if info[i] == score[i] == 0:
                continue
            if info[i] < score[i]:
                ryonScore += i
            else:
                apeachScore += i

        if apeachScore < ryonScore:
            global result, answer
            if answer < ryonScore - apeachScore:
                answer = ryonScore - apeachScore
                result = score[:]
        return
    for i in range(n, -1, -1):
        score[index] += i
        dfs(info, score, n - i, index + 1)
        score[index] -= i

def solution(n, info):
    info.reverse()
    ryonScore = [0] * 11
    dfs(info, ryonScore, n, 0)

    if not result:
        return [-1]

    return list(reversed(result))

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))
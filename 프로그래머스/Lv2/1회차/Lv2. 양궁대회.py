# TODO 틀림 '라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.'

import math
from itertools import combinations_with_replacement

def solution(n, info):
    result = [0] * 11

    info.reverse()
    maxDiffScore = 0
    for i in combinations_with_replacement([i for i in range(11)], n):
        tempApeach = info[:]
        tempRyon = [0] * 11
        for j in i:
            tempRyon[j] += 1
        # if tempRyon[10] == 1 and tempRyon[9] == 1 and tempRyon[8] == 1 and tempRyon[7] == 1 and tempRyon[6] == 1 and tempRyon[5] == 1 and tempRyon[4] == 1 and tempRyon[3] == 1 and tempRyon[2] == 0:
        #     print(1)
        matchResult = []
        for apeach, ryon in zip(tempApeach, tempRyon):
            if apeach == 0 and ryon == 0:
                matchResult.append(math.inf)
            else:
                matchResult.append(apeach - ryon)

        apeachScore = sum([idx for idx, value in enumerate(matchResult) if 0 <= value and value != math.inf])
        ryonScore = sum([idx for idx, value in enumerate(matchResult) if value < 0])
        if apeachScore < ryonScore and maxDiffScore <= ryonScore - apeachScore:
            temp = [0] * 11
            for j in i:
                temp[j] += 1
            for j in range(len(temp)):
                if result[j] < temp[j]:
                    maxDiffScore = max(maxDiffScore, ryonScore - apeachScore)
                    result = temp[:]
                    break
    result.reverse()
    if result.count(0) == 11:
        return [-1]
    return result

# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
# print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))
# print(solution(10, [0,9,0,0,0,0,0,0,1,0,0]))
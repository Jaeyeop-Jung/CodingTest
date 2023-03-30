import math

dic = {'diamond': 0, 'iron': 1, 'stone': 2}

cost = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]


def dfs(minerals, picks, idx, total):
    if picks == [0, 0, 0] or idx == len(minerals):
        global result
        result = min(result, total)
        return

    for i in range(3):
        if 0 < picks[i]:
            picks[i] -= 1
            temp = 0
            for cnt in range(5):
                if len(minerals) <= idx + cnt:
                    break
                temp += cost[i][dic[minerals[idx + cnt]]]
            dfs(minerals, picks, idx + cnt + 1, total + temp)
            picks[i] += 1


result = math.inf


def solution(picks, minerals):
    dfs(minerals, picks, 0, 0)
    return result

print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
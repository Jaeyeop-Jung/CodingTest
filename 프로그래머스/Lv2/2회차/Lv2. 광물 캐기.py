import math

res = math.inf
dic = {
    0: {'diamond': 1, 'iron': 1, 'stone': 1},
    1: {'diamond': 5, 'iron': 1, 'stone': 1},
    2: {'diamond': 25, 'iron': 5, 'stone': 1}
}

def dfs(picks, minerals, idx, cnt, cur, cost):
    if idx == len(minerals) or (sum(picks) == 0 and cnt == 5):
        global res
        res = min(res, cost)
        return

    cnt %= 5
    if cnt != 0:
        dfs(picks, minerals, idx + 1, cnt + 1, cur, cost + dic[cur][minerals[idx]])
    else:
        for i in range(3):
            if not picks[i]:
                continue
            picks[i] -= 1
            dfs(picks, minerals, idx + 1, 1, i, cost + dic[i][minerals[idx]])
            picks[i] += 1


def solution(picks, minerals):
    global res
    res = math.inf
    dfs(picks, minerals, 0, 0, -1, 0)
    return res

# print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))
print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))
print(solution([1, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond", "diamond", "diamond", "diamond", "diamond"]))
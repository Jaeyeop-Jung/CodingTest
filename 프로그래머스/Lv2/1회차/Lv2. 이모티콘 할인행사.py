
discount = [10, 20, 30, 40]

def dfs(users, emoticons, idx, cost):
    if idx == len(emoticons):
        global resPlus
        global resCost
        tempPlus, tempCost = cal(users, emoticons, cost)
        if resPlus < tempPlus or (resPlus == tempPlus and resCost <= tempCost):
            resPlus, resCost = tempPlus, tempCost
        return

    for i in range(len(discount)):
        dfs(users, emoticons, idx + 1, cost + [[idx, discount[i]]])

def cal(users, emoticons, cost):
    val = [[emoticons[cost[i][0]] * ((100 - cost[i][1]) / 100), cost[i][1]] for i in range(len(cost))]
    tempPlus, tempCost = 0, 0
    for boundary, buyCost in users:
        totalBuyCost = sum([val[i][0] for i in range(len(val)) if boundary <= val[i][1]])
        if buyCost <= totalBuyCost:
            tempPlus += 1
        else:
            tempCost += totalBuyCost
    return tempPlus, int(tempCost)


resPlus, resCost = 0, 0
def solution(users, emoticons):
    dfs(users, emoticons, 0, [])
    return [resPlus, resCost]


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
# print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
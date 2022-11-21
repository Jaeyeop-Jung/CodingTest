
def sell(dic, seller, amount):
    if len(dic[seller]) == 1:
        dic[seller][0] += amount
        return

    if amount * 0.9 < 1:
        dic[seller][1] += amount
        return
    else:
        dic[seller][1] += amount - amount // 10
        sell(dic, dic[seller][0], amount // 10)

def solution(enroll, referral, seller, amount):
    dic = {'-': [0]}
    for i in range(len(enroll)):
        dic[enroll[i]] = [referral[i], 0]
    for i in range(len(seller)):
        sell(dic, seller[i], amount[i] * 100)

    del dic['-']
    return [round(dic[i][1]) for i in dic]


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))

# TODO 틀림 깊게 고민

def solution(enroll, referral, seller, amount):
    dic = {}
    dic['center'] = ['-', 0]
    for i in range(len(referral)):
        if referral[i] == '-':
            dic[enroll[i]] = ['center', 0]
        else:
            dic[enroll[i]] = [referral[i], 0]
    amount = [i * 100 for i in amount]

    for i in range(len(seller)):
        dic[seller[i]][1] += amount[i] - amount[i] // 10
        tempParent = dic[seller[i]][0]
        tempAmount = amount[i] // 10
        while True:
            if tempParent == 'center' or tempAmount == 0:
                break
            dic[tempParent][1] += tempAmount - tempAmount // 10
            tempParent = dic[tempParent][0]
            tempAmount = tempAmount // 10

    del dic['center']
    return [dic[i][1] for i in dic]

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
# print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]))
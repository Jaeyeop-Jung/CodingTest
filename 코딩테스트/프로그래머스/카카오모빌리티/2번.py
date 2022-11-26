

def solution(id_list, k):
    numberOfCouponEachUser = {}
    result = 0
    for each_id_list in id_list:
        id_list_by_day = set(each_id_list.split(' '))
        for id in id_list_by_day:
            if id in numberOfCouponEachUser and numberOfCouponEachUser[id] < k:
                numberOfCouponEachUser[id] += 1
                result += 1
            elif id not in numberOfCouponEachUser:
                numberOfCouponEachUser[id] = 1
                result += 1
    return result



# print(solution(["A B C D", "A D", "A B D", "B D"], 2))
print(solution(["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3))




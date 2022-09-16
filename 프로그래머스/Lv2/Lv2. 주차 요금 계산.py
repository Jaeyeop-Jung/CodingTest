import math


def solution(fees, records):
    cost = {}
    for i in records:
        time, carNum, status = i.split(' ')
        if status == 'IN':
            if carNum not in cost:
                cost[carNum] = [time, status, 0]
            else:
                cost[carNum] = [time, status, cost[carNum][2]]
        else:
            inHour, inMinute = map(int, cost[carNum][0].split(':'))
            outHour, outMinute = map(int, time.split(':'))
            parkedMinute = (outHour - inHour) * 60 + outMinute - inMinute
            cost[carNum] = ['0', status, cost[carNum][2] + parkedMinute]
    for i in cost:
        if cost[i][1] == 'IN':
            inHour, inMinute, = map(int, cost[i][0].split(':'))
            cost[i][2] += (23 - inHour) * 60 + 59 - inMinute

    result = []
    keys = sorted(list(cost.keys()))
    for i in keys:
        if cost[i][2] <= fees[0]:
            result.append(fees[1])
        else:
            result.append(fees[1] + int(math.ceil((cost[i][2] - fees[0]) / fees[2])) * fees[3])
    return result


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
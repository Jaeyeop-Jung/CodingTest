
def checkAllZero(arr):
    for i in arr:
        if i != 0:
            return False
    return True

def solution(cap, n, deliveries, pickups):
    result = 0

    if checkAllZero(deliveries) and checkAllZero(pickups):
        return 0

    while deliveries or pickups:
        length = max(len(deliveries), len(pickups))

        idx = len(deliveries) - 1
        tempCap = cap
        while tempCap != 0 and 0 <= idx:
            if deliveries[idx] <= tempCap:
                tempCap -= deliveries[idx]
                deliveries[idx] = 0
            else:
                deliveries[idx] -= tempCap
                tempCap = 0
            idx -= 1

        idx = len(pickups) - 1
        tempCap = cap
        while tempCap != 0 and 0 <= idx:
            if pickups[idx] <= tempCap:
                tempCap -= pickups[idx]
                pickups[idx] = 0
            else:
                pickups[idx] -= tempCap
                tempCap = 0
            idx -= 1

        while deliveries and deliveries[-1] == 0:
            deliveries.pop()
        while pickups and pickups[-1] == 0:
            pickups.pop()

        result += length * 2

    return result


# print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
# print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
# print(solution(3, 4, [2, 1, 0, 2], [1, 1, 0, 2]))
# print(solution(4, 6, [4, 1, 3, 2, 1, 0], [1, 1, 2, 0, 1, 2]))
print(solution(1, 1, [0], [0]))
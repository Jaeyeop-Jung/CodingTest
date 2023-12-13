
def solution(weather, capacity):
    cur = 0
    res = 0
    for day in range(len(weather)):
        # 흐리면
        if weather[day] == 1:
            if 0 < cur:
                res += 1
                cur -= 1
            else:
                break
        # 맑으면
        else:
            # 전날 발동 안함
            if day - 1 < 0 or weather[day - 1] == 1:
                # 근데 지금 캐파가 1보다 커
                if 1 < cur:
                    res += 1
                    cur -= 1
                # 아니면
                else:
                    res += 1
                    cur = 1
            else:
                res += 1
                cur += 1
        if capacity <= cur:
            cur = capacity
    return res

# print(solution([0, 1, 0, 0, 0, 1, 1], 100))
# print(solution([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1], 10))
# print(solution([0, 0, 0, 1, 1, 1], 2))
# print(solution([0, 0, 1, 1, 1, 1], 50))
# print(solution([1, 0, 0, 0], 10000))
print(solution([0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], 10000))
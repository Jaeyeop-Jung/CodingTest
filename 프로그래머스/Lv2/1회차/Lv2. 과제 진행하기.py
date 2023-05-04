from collections import deque

def solution(plans):
    plans.sort(key=lambda x: x[1])
    plans = [[name, int(startTime.split(':')[0]) * 60 + int(startTime.split(':')[1]), int(rest)] for name, startTime, rest in plans]
    plans = deque(plans)
    wait = []

    result = []
    while plans:
        name, startTime, rest, = plans.popleft()
        endTime = startTime + rest
        if plans and plans[0][1] < endTime: # 끝내기 불가능하면
            nextStartTime = plans[0][1]
            wait.append([name, nextStartTime, endTime - nextStartTime])
        else:   # 끝내기 가능
            result.append(name)
            if plans and plans[0][1] == endTime:
                pass
            else:
                if wait:
                    name, _, rest = wait.pop()
                    plans.appendleft([name, endTime, rest])

    return result

print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
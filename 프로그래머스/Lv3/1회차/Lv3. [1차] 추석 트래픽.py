# TODO 틀림

def get_time(line):
    line = list(line.split())
    hour, minute, second, millisecond = int(line[1][:2]), int(line[1][3:5]), int(line[1][6:8]), int(line[1][9:])
    t = float(line[2][:-1]) * 1000 - 1
    endTime = (hour * 60 * 60 * 1000) + (minute * 60 * 1000) + (second * 1000) + millisecond
    startTime = endTime - t

    return (startTime, endTime)

def solution(lines):
    answer = 0
    times = []

    for line in lines:
        times.append(get_time(line))

    for i in range(len(times)):
        cnt = 0
        for j in range(i, len(times)):
            if times[i][1] + 1000 > times[j][0]:
                cnt += 1

        answer = max(answer, cnt)
    return answer


# print(solution([
#     "2016-09-15 01:00:04.001 2.0s",
#     "2016-09-15 01:00:07.000 2s"
# ]))
#
# print(solution([
#     "2016-09-15 01:00:04.002 2.0s",
#     "2016-09-15 01:00:07.000 2s"
# ]))

print(solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]))

# print(solution(["2016-09-15 23:59:59.999 0.001s"]))
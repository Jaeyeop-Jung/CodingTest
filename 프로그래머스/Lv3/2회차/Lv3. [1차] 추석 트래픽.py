# TODO 틀림

def toMili(time, t):
    hour, minute, second = time.split(':')
    second, millisecond = second.split('.')
    millisecond = int(millisecond)

    millisecond += 1000 * int(second)
    millisecond += 1000 * 60 * int(minute)
    millisecond += 1000 * 60 * 60 * int(hour)

    millisecond -= int(float(t[:-1]) * 1000)
    return millisecond

def solution(lines):
    result = 1
    startTime = []
    endTime = []
    for line in lines:
        _, time, t, = line.split()
        startTime.append(toMili(time, t) + 1)
        endTime.append(toMili(time, '0s'))

    for i in range(len(lines)):
        tempS = 0
        tempE = 0
        end = endTime[i]
        for j in range(len(lines)):
            startCompare = startTime[j]
            endCompare = endTime[j]

            if startTime[i] <= startCompare < startTime[i] + 1000:
                tempS += 1
            elif startTime[i] <= endCompare < startTime[i] + 1000:
                tempS += 1
            elif startCompare <= startTime[i] < startTime[i] + 1000 <= endCompare:
                tempS += 1

            if end <= startCompare < end + 1000:
                tempE += 1
            elif end <= endCompare < end + 1000:
                tempE += 1
            elif startCompare <= end < end + 1000 <= endCompare:
                tempE += 1

            # if startTime[i] <= endCompare and startCompare < startTime[i] + 1000:
            #     tempS += 1
            # if end <= endCompare and startCompare < end + 1000:
            #     tempE += 1

        result = max(result, tempS, tempE)

    return result

# print(solution([
# "2016-09-15 20:59:57.421 0.351s",
# "2016-09-15 20:59:58.233 1.181s",
# "2016-09-15 20:59:58.299 0.8s",
# "2016-09-15 20:59:58.688 1.041s",
# "2016-09-15 20:59:59.591 1.412s",
# "2016-09-15 21:00:00.464 1.466s",
# "2016-09-15 21:00:00.741 1.581s",
# "2016-09-15 21:00:00.748 2.31s",
# "2016-09-15 21:00:00.966 0.381s",
# "2016-09-15 21:00:02.066 2.62s"
# ]))
# print(solution([
# "2016-09-15 01:00:04.001 2.0s",
# "2016-09-15 01:00:07.000 2s"
# ]))
print(solution([
'2016-09-15 00:00:00.000 3s'
]))
# TODO 틀림 다음엔 맞자

def solution(lines):
    milliseconds = []
    for i in range(len(lines)):
        _, time, add, = lines[i].split()
        before, temp = time.split('.')
        temp = int(temp)
        before = list(map(int, before.split(':')))
        temp += before[2] * 1000 + before[1] * 1000 * 60 + before[0] * 1000 * 60 * 60
        milliseconds.append([temp - int(float(add[:-1]) * 1000) + 1, temp])

    milliseconds.sort()
    res = 1
    for i in range(len(milliseconds)):
        start, end = milliseconds[i]

        temp1 = 0
        limit = start + 999
        for j in range(len(milliseconds)):
            afterStart, afterEnd, = milliseconds[j]
            if start <= afterStart <= limit or start <= afterEnd <= limit or afterStart <= start <= afterEnd:
                temp1 += 1

        temp2 = 0
        limit = end + 999
        for j in range(len(milliseconds)):
            afterStart, afterEnd, = milliseconds[j]
            if end <= afterStart <= limit or end <= afterEnd <= limit or afterStart <= end <= afterEnd:
                temp2 += 1

        res = max(res, temp1, temp2)


    return res

print(solution(	["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
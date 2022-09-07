def solution(progresses, speeds):
    result = []
    workTime = []

    for i in range(len(progresses)):
        leftTime = 100 - progresses[i]
        leftDay = 0
        if leftTime % speeds[i] != 0:
            leftDay = leftTime // speeds[i] + 1
        else:
            leftDay = leftTime // speeds[i]

        if workTime:
            if workTime[0] < leftDay:
                result.append(len(workTime))
                workTime.clear()
        workTime.append(leftDay)
    result.append(len(workTime))

    return result

solution(	[93, 30, 55, 60, 40, 65], [1, 30, 5, 10, 60, 7])
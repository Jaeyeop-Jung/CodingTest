
import datetime

def strToDateTime(time):
    if time[:2] != '00':
        return datetime.datetime.strptime(time, '%d:%H:%M:%S')
    elif time[3:5] != '00':
        return datetime.datetime.strptime(time[3:], '%H:%M:%S')
    elif time[6:8] != '00':
        return datetime.datetime.strptime(time[6:], '%M:%S')
    else:
        return datetime.datetime.strptime(time[9:], '%S')

def addTerm(time, term, isDiffDay):
    if isDiffDay:
        time += datetime.timedelta(days=term.day)
    time += datetime.timedelta(hours=term.hour)
    time += datetime.timedelta(minutes=term.minute)
    time += datetime.timedelta(seconds=term.second)
    return time

def isContinuous(preTime, postTime):
    standardTime = preTime + datetime.timedelta(days=1)
    if standardTime.year == postTime.year \
        and standardTime.month == postTime.month \
        and preTime.day == postTime.day:
        return 1
    elif standardTime.year == postTime.year \
        and standardTime.month == postTime.month \
        and standardTime.day == postTime.day:
        return 1
    return 0


def solution(s, times):
    saveTimes = [datetime.datetime.strptime(s, '%Y:%m:%d:%H:%M:%S')]
    oneDayOneSave = 1
    period = 1
    for eachTime in times:
        # 걸린 기간 더하기
        term = strToDateTime(eachTime)
        if 0 < int(eachTime[:2]):
            saveTimes.append(addTerm(saveTimes[-1], term, True))
        else:
            saveTimes.append(addTerm(saveTimes[-1], term, False))

        # 1일 1저축 확인
        oneDayOneSave = isContinuous(saveTimes[-2], saveTimes[-1])

        # 기간 확인
        period += saveTimes[-1].day - saveTimes[-2].day

    return [oneDayOneSave, period]


print(solution("2021:04:12:16:08:35", ["01:06:30:00", "01:04:12:00"]))
print(solution("2021:04:12:16:08:35", ["01:06:30:00", "00:01:12:00"]))




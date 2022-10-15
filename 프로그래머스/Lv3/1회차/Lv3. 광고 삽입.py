# TODO 틀림 아이디어, 구현 더 집중

def getTime(sec):
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    h, m, s = str(h), str(m), str(s)
    result = ''
    for i in [h, m, s]:
        if len(i) == 1:
            result += '0' + i
        else:
            result += i
        result += ':'
    return result[:-1]

def getSec(hour, min, sec):
    return int(hour) * 60 ** 2 + int(min) * 60 + int(sec)

def solution(play_time, adv_time, logs):
    playHour, playMin, playSec = map(int, play_time.split(':'))
    totalPlaySec = playHour * 60 ** 2 + playMin * 60 + playSec
    advHour, advMin, advSec = map(int, adv_time.split(':'))
    totalAdvSec = advHour * 60 ** 2 + advMin * 60 + advSec
    viewer = [0] * (totalPlaySec + 1)

    for log in logs:
        startTime, endTime = log.split('-')
        startHour, startMin, startSec, = startTime.split(':')
        endHour, endMin, endSec, = endTime.split(':')
        viewer[getSec(startHour, startMin, startSec)] += 1
        viewer[getSec(endHour, endMin, endSec)] -= 1

    temp = 0
    if viewer[0] != 0:
        temp += viewer[0]
        viewer[0] += temp
    for i in range(1, totalPlaySec):
        temp += viewer[i]
        viewer[i] = temp
        viewer[i] += viewer[i - 1]

    start, maxScore = 0, 0
    for i in range(0, totalPlaySec - totalAdvSec):
        if maxScore < viewer[i + totalAdvSec] - viewer[i]:
            start = i
            maxScore = viewer[i + totalAdvSec] - viewer[i]

    if start == 0:
        return '00:00:00'
    else:
        return getTime(start + 1)


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
# print(solution('00:00:10', '00:00:03', ['00:00:01-00:00:10', '00:00:03-00:00:05']))
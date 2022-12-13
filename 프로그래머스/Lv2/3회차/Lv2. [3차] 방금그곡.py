
def replace(string):
    return string.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

def getDiffTime(startTime, endTime):
    startHour, startMinute = startTime.split(':')
    endHour, endMinute, = endTime.split(':')
    return (int(endHour) - int(startHour)) * 60 + int(endMinute) - int(startMinute)


def solution(m, musicinfos):
    m = replace(m)
    result = []
    for i, musicinfo in enumerate(musicinfos):
        startTime, endTime, subject, info, = musicinfo.split(',')
        info = replace(info)

        # 들은 악보와 재생된 악보가 아예 다를 때
        diffMinute = getDiffTime(startTime, endTime)
        playingInfo = (info * diffMinute)[:diffMinute]
        if m not in playingInfo:
            continue

        result.append([diffMinute, i, subject])

    if not result:
        return '(None)'
    result.sort(key=lambda x: (-x[0], x[1]))
    return result[0][2]




print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
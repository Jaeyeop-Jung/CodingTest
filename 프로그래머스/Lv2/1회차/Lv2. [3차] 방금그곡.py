# TODO 틀림 https://school.programmers.co.kr/questions/19633

from datetime import datetime

shopChange = {
    'C#' : 'c',
    'D#' : 'd',
    'F#' : 'f',
    'G#' : 'g',
    'A#' : 'a',
    'E#' : 'e'
}

def solution(m, musicinfos):
    for i in shopChange:
        m = m.replace(i, shopChange[i])

    musicSinging = []
    for i, info in enumerate(musicinfos):
        startTime, endTime, name, musicInfo = info.split(',')
        singingMinute = (datetime.strptime(endTime, '%H:%M') - datetime.strptime(startTime, '%H:%M')).seconds // 60
        for j in shopChange:
            musicInfo = musicInfo.replace(j, shopChange[j])
        musicSinging.append([(((singingMinute // len(musicInfo)) + 1) * musicInfo)[:singingMinute], singingMinute, name])

    musicSinging = [musicSinging[i] for i in range(len(musicSinging)) if m in musicSinging[i][0]]
    if not musicSinging:
        return '(None)'

    maxMinute = max([musicSinging[i][1] for i in range(len(musicSinging))])
    musicSinging = [musicSinging[i] for i in range(len(musicSinging)) if musicSinging[i][1] == maxMinute]
    if not musicSinging:
        return '(None)'

    return musicSinging[0][2]


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("C", ["13:00,13:01,WORLD,F"]))

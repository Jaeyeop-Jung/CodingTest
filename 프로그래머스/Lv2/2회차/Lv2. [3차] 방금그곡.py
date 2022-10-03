# TODO 틀림 10, 19번 케이스만 틀리는데 이유를 모르겠음..

dic = {
    'C#':'c',
    'D#':'d',
    'F#':'f',
    'G#':'g',
    'A#':'a',
    'E#':'e'
}

def solution(m, musicinfos):
    m = m.replace('C#', dic['C#']).replace('D#', dic['D#']).replace('F#', dic['F#']).replace('G#', dic['G#']).replace('A#', dic['A#']).replace('E#', dic['E#'])
    data = []
    for idx, value in enumerate(musicinfos):
        startTime, endTime, name, info = value.split(',')
        info = info.replace('C#', dic['C#']).replace('D#', dic['D#']).replace('F#', dic['F#']).replace('G#', dic['G#']).replace('A#', dic['A#']).replace('E#', dic['E#'])
        diffHour, diffMin = int(endTime.split(':')[0]) - int(startTime.split(':')[0]), int(endTime.split(':')[1]) - int(startTime.split(':')[1])
        if diffHour * 60 + diffMin < len(m):
            continue
        if m not in (info * (len(info) + 1))[:diffHour * 60 + diffMin]:
            continue
        data.append([idx, diffHour * 60 + diffMin, name, (info * (len(info) + 1))[:diffHour * 60 + diffMin]])

    data.sort(key=lambda x: (-x[1], x[0]))

    if not data:
        return '(None)'
    return data[0][2]


# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABC", ["12:00,12:14,HELLO,ABCABC", "13:00,13:14,WORLD,ABCCAB"]))

def toString(time):
    hour = str(time // 60)
    minute = str(time % 60)
    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute
    return hour + ':' + minute

def solution(n, t, m, timetable):
    timetable.sort()
    timetable = [int(i.split(':')[0]) * 60 + int(i.split(':')[1]) for i in timetable]
    bus = 9 * 60

    for i in range(n - 1):
        for j in range(m):
            if not timetable:
                return toString(bus)
            if timetable[0] <= bus:
                timetable.pop(0)
        bus += t

    for i in range(m - 1):
        if not timetable:
            return toString(bus)
        if timetable[0] <= bus:
            timetable.pop(0)

    if not timetable or bus < timetable[0]:
        return toString(bus)
    return toString(timetable[0] - 1)



print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))

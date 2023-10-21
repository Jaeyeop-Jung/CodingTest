

def extractErrorLogs(logs):
    arr = []
    for i, v in enumerate(logs):
        d1, time, msg, status = v
        if msg == 'ERROR' or msg == 'CRITICAL':
            day, month, year, = d1.split('-')

            arr.append([year + month + day + time, i, d1, time, msg, status])

    arr.sort()
    res = []
    for time, _, d1, t2, msg, status in arr:
        res.append([d1, t2, msg, status])
    return res


print(extractErrorLogs([['01-01-2022', '18:00', 'CRITICAL', 'failed'],
['01-01-2023', '15:00', 'ERROR', 'failed'],
['01-01-2023', '16:00', 'SUCCESS', 'established']]))
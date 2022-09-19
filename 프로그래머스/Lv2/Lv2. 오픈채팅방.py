
def solution(record):
    result = []
    nameDict = {}
    for i in range(len(record)):
        if record[i].startswith('E') or record[i].startswith('C'):
            status, id, name = record[i].split(' ')
            nameDict[id] = name
    for i in record:
        if i.startswith('E'):
            status, id, name = i.split(' ')
            result.append(nameDict[id] + '님이 들어왔습니다.')
        elif i.startswith('L'):
            status, id = i.split(' ')
            result.append(nameDict[id] + '님이 나갔습니다.')

    return result



print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
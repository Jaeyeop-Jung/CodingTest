
def solution(s):
    arr = s.split(' ')
    for i in range(len(arr)):
        if arr[i] == '':
            continue
        elif arr[i][0].isalpha() is True:
            arr[i] = arr[i][0].upper() + arr[i][1:].lower()
        else:
            arr[i] = arr[i].lower()
    return ' '.join(arr)

print(solution("3peoPle afw"))
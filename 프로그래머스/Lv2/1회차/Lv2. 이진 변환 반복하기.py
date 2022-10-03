def solution(s):
    count = 0
    removedZero = 0

    while s != '1':
        data = ''
        for i in s:
            if i == '0':
                removedZero += 1
            else:
                data += i
        data = format(len(data), 'b')
        s = data
        count += 1

    return [count, removedZero]
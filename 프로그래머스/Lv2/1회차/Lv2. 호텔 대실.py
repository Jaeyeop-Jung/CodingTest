from collections import deque

cleanTime = 10 * 60

def toSecond(time):
    h, m, = time.split(':')
    return int(h) * 3600 + int(m) * 60

def solution(book_time):
    for i in range(len(book_time)):
        book_time[i] = [toSecond(book_time[i][0]), toSecond(book_time[i][1])]
    book_time.sort()

    q = deque(book_time)
    cur = []
    result = 0
    while q:
        start, end, = q.popleft()

        # 퇴실
        for i in range(len(cur) - 1, -1, -1):
            if cur[i][1] + cleanTime <= start:
                cur.pop(i)

        # 입실
        cur.append([start, end])

        result = max(result, len(cur))

    return result


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))

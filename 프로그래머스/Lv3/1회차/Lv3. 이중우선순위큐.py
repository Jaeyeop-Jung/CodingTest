import heapq

def solution(operations):
    h = []
    for i in operations:
        status, num = i.split(' ')
        if status == 'I':
            heapq.heappush(h, int(num))
        elif status == 'D' and num == '1':
            if h:
                h.pop(h.index(max(h)))
        else:
            if h:
                heapq.heappop(h)
    if not h:
        return [0,0]
    else:
        return [max(h), heapq.heappop(h)]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
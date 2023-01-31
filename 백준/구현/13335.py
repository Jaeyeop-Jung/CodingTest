from collections import deque

n, l, w = map(int, input().split())
rest = deque(list(map(int, input().split())))

cur = deque()
cur_weight = 0
i = 1
while True:
    # 다리 넘어가기
    if cur and l == i - cur[0][1]:
        pop = cur.popleft()
        cur_weight -= pop[0]

    # 다리 들어가기
    if rest and rest[0] + cur_weight <= w:
        pop = rest.popleft()
        cur.append([pop, i])
        cur_weight += pop

    # 끝났는가
    if not cur and not rest:
        print(i)
        break
    i += 1
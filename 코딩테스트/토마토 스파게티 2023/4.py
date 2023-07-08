from collections import deque

def move(res, maxSize, next):
    # 중복
    if next in res:
        res.remove(next)
        res.append(next)
        return

    # 맥스 사이즈
    if len(res) == maxSize:
        res.popleft()
        res.append(next)
        return

    # 맥스 사이즈 X
    res.append(next)

def solution(maxSize, actions):
    before = deque()
    forward = deque()
    res = deque()

    for action in actions:
        # 이동
        if action.isnumeric():
            if res:
                before.append(res[-1])
            move(res, maxSize, action)
            forward = deque()

        # 뒤로 가기
        if action == 'B':
            if not before:
                continue
            pop = before.pop()
            next = res[-1]
            move(res, maxSize, pop)
            forward.append(next)

        # 앞으로 가기
        if action == 'F':
            if not forward:
                continue
            pop = forward.pop()
            before.append(pop)
            move(res, maxSize, pop)

    return list(reversed(res))


# print(solution(3, ["1", "2", "3", "4", "5"]))
# print(solution(3, ["1", "2", "3", "4", "3"]))
# print(solution(3, ["1", "3", "2", "B", "4", "F"]))
# print(solution(3, ["1", "3", "2", "B", "4", "F"]))
print(solution(3, ["1", "2", "B", "F"]))
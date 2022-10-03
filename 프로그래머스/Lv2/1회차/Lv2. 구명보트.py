# TODO 틀림 https://velog.io/@daon9apples/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level-2-%EA%B5%AC%EB%AA%85%EB%B3%B4%ED%8A%B8-python

# def solution(people, limit):
#     result = 0
#     people.sort()
#
#     maxIndex = -1
#     for i in range(len(people) - 1):
#         maxIndex = -1
#         for j in range(i + 1, len(people)):
#             if people[i] + people[j] <= limit:
#                 maxIndex = j
#             else:
#                 if maxIndex != -1:
#                     result += 1
#                     people.pop(maxIndex)
#                     people.pop(i)
#                     break
#
#     return result + len(people)

from collections import deque

def solution(people, limit):
    result = 0
    people.sort()
    queue = deque(people)

    while queue:
        if 2 <= len(queue):
            if queue[0] + queue[-1] <= limit:
                queue.pop()
                queue.popleft()
            else:
                queue.pop()
            result += 1
        else:
            if queue[0] <= limit:
                queue.pop()
                result += 1
    return result


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
from collections import deque

def solution(people, limit):
    people.sort(reverse=True)
    people = deque(people)
    result = 0
    while True:
        if len(people) == 1:
            result += 1
            break
        elif len(people) == 0:
            break

        if people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
            result += 1
        else:
            people.popleft()
            result += 1

    return result

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
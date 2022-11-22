# TODO 틀림

import re
from itertools import permutations

def solution(user_id, banned_id):
    n = len(banned_id)
    for i in range(n):
        banned_id[i] = banned_id[i].replace('*', '.')

    result = set()
    for i in permutations(user_id, n):
        visited = [False] * n
        temp = list(i)
        for j in range(len(banned_id)):
            for k in range(len(temp)):
                if re.fullmatch(banned_id[j], temp[k]) and not visited[k]:
                    visited[k] = True
                    break
        if visited.count(False) == 0:
            temp.sort()
            result.add(tuple(temp))
    return len(result)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))



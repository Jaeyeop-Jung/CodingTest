# TODO 틀림

import re
from itertools import product

def solution(user_id, banned_id):
    matched = [[] for i in range(len(banned_id))]
    banned_id = [i.replace('*', '\w') for i in banned_id]

    for idx, value in enumerate(banned_id):
        for j in user_id:
            if re.match('^' + value + '$', j) != None:
                matched[idx].append(j)

    result = set()
    for i in list(product(*matched)):
        if len(set(i)) == len(matched):
            result.add(tuple(sorted(i)))
    return len(result)




print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))


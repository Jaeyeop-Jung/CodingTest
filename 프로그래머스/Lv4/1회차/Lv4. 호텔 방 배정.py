# TODO 틀림

import sys
sys.setrecursionlimit(10 ** 7)

def find_parent(parent, x):
    if x not in parent:
        return x
    else:
        return find_parent(parent, parent[x])


def solution(k, room_number):
    result = []
    parent = {}
    for i in range(len(room_number)):
        roomNumber = find_parent(parent, room_number[i])
        parent[roomNumber] = parent[roomNumber + 1] if roomNumber + 1 in parent else roomNumber + 1
        result.append(roomNumber)

    return result


print(solution(10, [1,3,4,1,3,1]))
print(solution(10, [1,2,3,4,5,6]))

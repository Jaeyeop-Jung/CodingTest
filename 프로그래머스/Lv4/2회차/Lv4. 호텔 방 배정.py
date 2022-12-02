# TODO 틀림 아이디어는 맞았는데 최적화를 더 잘해봐

import sys
sys.setrecursionlimit(10 ** 5)

def find_parent(parent, x):
    if x not in parent:
        return x
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

def solution(k, room_number):
    result = []
    parent = {}
    room_number = [0] + room_number

    for i in range(1, len(room_number)):
        room = find_parent(parent, room_number[i])
        result.append(room)
        union_parent(parent, parent[room], parent[room + 1])

    return result

print(solution(10, [1,3,4,1,3,1]))


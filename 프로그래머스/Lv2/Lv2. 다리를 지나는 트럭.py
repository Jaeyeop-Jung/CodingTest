from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque()
    truck = deque(truck_weights)
    for i in range(bridge_length * len(truck_weights) * 2):
        for j in range(len(q)):
            q[j][1] += 1
        if q and q[0][1] == bridge_length:
            q.popleft()
        if truck and sum([q[i][0] for i in range(len(q))]) + truck[0] <= weight:
            q.append([truck.popleft(), 0])
        if not truck and not q:
            return i + 1


print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
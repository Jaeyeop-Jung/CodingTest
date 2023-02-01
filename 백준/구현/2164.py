from collections import deque

n = int(input())
q = deque([i for i in range(n, 0, -1)])

while len(q) != 1:
    q.pop()
    q.appendleft(q.pop())
print(q[0])
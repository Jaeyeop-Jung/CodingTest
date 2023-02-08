from collections import deque

n, k, = map(int, input().split())
arr = list(map(int, input().split()))

up = deque(arr[:n])
down = deque(arr[n:][::-1])

robotUp = deque([False] * n)

def downRobot():
    global robotUp
    if robotUp[-1]:
        robotUp[-1] = False

result = 1
while True:

    # 1
    down.append(up.pop())
    up.appendleft(down.popleft())
    robotUp.rotate(1)
    downRobot()

    # 2
    for i in range(n - 2, -1, -1):
        if robotUp[i]:
            if not robotUp[i + 1] and 0 < up[i + 1]:
                up[i + 1] -= 1
                robotUp[i + 1] = True
                robotUp[i] = False
                downRobot()

    # 3
    if 0 < up[0]:
        up[0] -= 1
        robotUp[0] = True

    # 4
    if k <= up.count(0) + down.count(0):
        break

    result += 1

print(result)
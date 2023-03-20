from collections import deque

direction = {'L': 1, 'R': -1}

n, m, q = map(int, input().split())
arr = [deque(map(int, input().split())) for _ in range(n)]


def inRange(r):
    if 0 <= r < n:
        return True
    return False


for _ in range(q):
    r, d = input().split()
    r = int(r)
    r -= 1

    queue = deque()

    arr[r].rotate(direction[d])
    up = False
    down = False
    for c in range(m):
        if inRange(r - 1) and arr[r - 1][c] == arr[r][c]:
            up = True
        if inRange(r + 1) and arr[r + 1][c] == arr[r][c]:
            down = True
    queue.append([up, r - 1, down, r + 1, -direction[d]])

    while queue:
        up, upR, down, downR, d = queue.popleft()
        if up:
            arr[upR].rotate(d)
        if down:
            arr[downR].rotate(d)

        upTemp = False
        downTemp = False
        for c in range(m):
            if up and inRange(upR - 1) and arr[upR - 1][c] == arr[upR][c]:
                upTemp = True
            if down and inRange(downR + 1) and arr[downR + 1][c] == arr[downR][c]:
                downTemp = True
        if upTemp or downTemp:
            queue.append([upTemp, upR - 1, downTemp, downR + 1, -d])

for i in arr:
    print(*i)







dR = [0, -1, 0, 1]
dC = [1, 0, -1, 0]
direction = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}

c, r = map(int, input().split())
n, m = map(int, input().split())
board = [[[] for _ in range(c)] for _ in range(r)]
robots = []
for i in range(n):
    rC, rR, d = input().split()
    robots.append([int(rR) - 1, int(rC) - 1, direction[d]])
    board[int(rR) - 1][int(rC) - 1].append(i + 1)

for i in range(m):
    robot, command, num = input().split()
    robot, num = int(robot) - 1, int(num)
    if command == 'F':
        for _ in range(num):
            curR, curC, d, = robots[robot]
            movedR, movedC = curR + dR[d], curC + dC[d]
            if not 0 <= movedR < r or not 0 <= movedC < c:
                print(f'Robot {robot + 1} crashes into the wall')
                exit()
            if board[movedR][movedC]:
                print(f'Robot {robot + 1} crashes into robot {board[movedR][movedC][0]}')
                exit()
            board[movedR][movedC].append(board[curR][curC].pop())
            robots[robot] = [movedR, movedC, d]

    elif command == 'L':
        for _ in range(num):
            curR, curC, d, = robots[robot]
            d -= 1
            d %= 4
            robots[robot] = [curR, curC, d]
    elif command == 'R':
        for _ in range(num):
            curR, curC, d, = robots[robot]
            d += 1
            d %= 4
            robots[robot] = [curR, curC, d]

print('OK')
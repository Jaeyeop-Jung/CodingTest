
n = int(input())
m = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    board[i][i] = 1
for i in range(n):
    for j in range(n):
        for k in range(n):
            if board[i][k] == 0 or board[k][j] == 0:
                continue
            board[i][j] = board[i][k] + board[k][j]
            board[j][i] = board[i][k] + board[k][j]

# print(board)
route = list(map(int, input().split()))
for i in range(len(route) - 1):
    cur = route[i]
    next = route[i + 1]
    if board[cur - 1][next - 1] == 0:
        print('NO')
        exit()
print('YES')


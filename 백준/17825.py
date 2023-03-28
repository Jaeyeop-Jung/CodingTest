# TOOD 틀림 근데 이건 문제가 좀..

board = {
    i: [i + 1] for i in range(22)
}
board[21] = [21]
board[5].append(22)
board[22] = [23]
board[23] = [24]
board[24] = [25]

board[10].append(26)
board[26] = [27]
board[27] = [25]

board[15].append(28)
board[28] = [29]
board[29] = [30]
board[30] = [25]

board[25] = [31]
board[31] = [32]
board[32] = [20]

score = [i * 2 for i in range(22)]
score[-1] = 0
score += [13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35]

arr = list(map(int, input().split()))

def move(cur, moveCnt):
    if len(board[cur]) == 2:
        cur = board[cur][1]
    else:
        cur = board[cur][0]
    for i in range(moveCnt - 1):
        cur = board[cur][0]
    return cur

def dfs(arr, location, cur, total):
    if cur == 10:
        global result
        result = max(result, total)
        return
    for i in range(4):
        origin = location[i]
        moveLocation = move(location[i], arr[cur])
        if moveLocation not in location or moveLocation == 21:
            location[i] = moveLocation
            dfs(arr, location, cur + 1, total + score[moveLocation])
            location[i] = origin

result = 0
dfs(arr, [0, 0, 0, 0], 0, 0)
print(result)
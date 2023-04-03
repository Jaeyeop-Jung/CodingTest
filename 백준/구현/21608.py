from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n = int(input())
arr = deque(list(map(int, input().split())) for _ in range(n ** 2))
board = [[[] for _ in range(n)] for _ in range(n)]
friends = {}

while arr:
    num, f1, f2, f3, f4 = arr.popleft()
    friends[num] = [f1, f2, f3, f4]
    curR, curC = 4, 4
    friendCnt = -1
    emptyCnt = -1
    for r in range(n - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            if board[r][c]:
                continue
            tempFriendCnt = 0
            tempEmptyCnt = 0
            for d in range(4):
                movedR, movedC = r + dR[d], c + dC[d]
                if not 0 <= movedR < n or not 0 <= movedC < n:
                    continue
                if board[movedR][movedC] in [f1, f2, f3, f4]:
                    tempFriendCnt += 1
                if not board[movedR][movedC]:
                    tempEmptyCnt += 1
            if friendCnt < tempFriendCnt or \
                    (friendCnt == tempFriendCnt and emptyCnt < tempEmptyCnt) or \
                    (friendCnt == tempFriendCnt and emptyCnt == tempEmptyCnt):
                curR, curC = r, c
                friendCnt = tempFriendCnt
                emptyCnt = tempEmptyCnt
    board[curR][curC] = num

result = 0
for r in range(n):
    for c in range(n):
        cnt = 0
        for d in range(4):
            movedR, movedC = r + dR[d], c + dC[d]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                continue
            if board[movedR][movedC] in friends[board[r][c]]:
                cnt += 1
        if cnt == 1:
            result += 1
        elif cnt == 2:
            result += 10
        elif cnt == 3:
            result += 100
        elif cnt == 4:
            result += 1000

print(result)
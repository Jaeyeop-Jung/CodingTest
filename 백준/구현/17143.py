import sys

input = sys.stdin.readline

dR = [-1, 1, 0, 0]
dC = [0, 0, 1, -1]

r, c, m = map(int, input().split())
sharks = {}
board = [[[] for _ in range(c)] for _ in range(r)]
for i in range(m):
    sharkR, sharkC, s, d, z = map(int, input().split())
    sharks[i] = [sharkR - 1, sharkC - 1, s, d - 1, z]
    board[sharkR - 1][sharkC - 1].append(i)

def reverse(d):
    if d % 2 == 1:
        return d - 1
    else:
        return d + 1

def catch(man):
    for i in range(r):
        if board[i][man]:
            global result
            result += sharks[board[i][man][0]][-1]
            del sharks[board[i][man][0]]
            board[i][man] = []
            break

def move():
    for i in sharks:
        sharkR, sharkC, s, d, z = sharks[i]
        board[sharkR][sharkC].remove(i)
        for _ in range(s):
            movedR, movedC = sharkR + dR[d], sharkC + dC[d]
            if not 0 <= movedR < r or not 0 <= movedC < c:
                d = reverse(d)
                movedR, movedC = sharkR + dR[d], sharkC + dC[d]
            sharkR, sharkC = movedR, movedC
        sharks[i] = [sharkR, sharkC, s, d, z]
        board[sharkR][sharkC].append(i)

def eat():
    for i in range(r):
        for j in range(c):
            if 2 <= len(board[i][j]):
                idxs = [idx for idx in board[i][j]]
                maxIdx = -1
                maxSize = -1
                for idx in idxs:
                    if maxSize < sharks[idx][-1]:
                        maxIdx = idx
                        maxSize = sharks[idx][-1]
                for idx in idxs:
                    if maxIdx != idx:
                        del sharks[idx]
                board[i][j] = [maxIdx]

result = 0
for man in range(c):
    catch(man)
    move()
    eat()

print(result)
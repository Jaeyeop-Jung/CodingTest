
dR = [1, 0, 0, -1]
dC = [0, -1, 1, 0]

def getResult(string):
    return string.replace('0', 'd').replace('1', 'l').replace('2', 'r').replace('3', 'u')

def canMove(n, m, move, r, c):
    nextR, nextC, = r + dR[move], c + dC[move]
    if not 1 <= nextR <= n or not 1 <= nextC <= m:
        return False
    return True

def move(move, r, c):
    return r + dR[move], c + dC[move]

def getDiff(x, y, r, c):
    return abs(r - x) + abs(c - y)

def solution(n, m, x, y, r, c, k):
    if k < abs(r - x) + abs(c - y):
        return 'impossible'
    if k % 2 != (abs(r - x) + abs(c - y))  % 2:
        return 'impossible'

    curR, curC = x, y
    result = ''
    while k != 0:
        for i in range(4):
            if canMove(n, m, i, curR, curC):
                movedR, movedC = move(i, curR, curC)
                if getDiff(movedR, movedC, r, c) <= k:
                    curR, curC = movedR, movedC
                    k -= 1
                    result += str(i)
                    break

    return getResult(result)



print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(5, 5, 1, 1, 2, 2, 8))
print(solution(5, 5, 4, 3, 2, 2, 7))

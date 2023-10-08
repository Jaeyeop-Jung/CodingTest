
dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

arr = [list(input()) for _ in range(5)]

def getNext(r, c):
    res = []
    for i in range(4):
        movedR, movedC = r + dR[i], c + dC[i]
        if not 0 <= movedR < 5 or not 0 <= movedC < 5:
            continue
        res.append((movedR, movedC))
    return res

def dfs(arr, go, y, s, cur):
    if y + s == 7:
        if 4 <= s:
            res.add(cur)
        return

    for i in range(len(go)):
        nR, nC, = go[i]
        if cur & 1 << (nR * 5 + nC):
            continue

        next = cur | 1 << (nR * 5 + nC)
        if arr[nR][nC] == 'Y':
            nextGo = go[:i] + go[i + 1:] + getNext(nR, nC)
            dfs(arr, nextGo, y + 1, s, next)
        else:
            nextGo = go[:i] + go[i + 1:] + getNext(nR, nC)
            dfs(arr, nextGo, y, s + 1, next)

res = set()
for r in range(5):
    for c in range(5):
        go = getNext(r, c)
        if arr[r][c] == 'Y':
            dfs(arr, go, 1, 0, 1 << r * 5 + c)
        else:
            dfs(arr, go,0, 1, 1 << r * 5 + c)

print(len(res))
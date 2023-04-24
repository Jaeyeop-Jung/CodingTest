from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

def solution(places):
    result = [1] * 5
    for idx, place in enumerate(places):
        flag = False
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':
                    q = deque([[r, c, 0]])
                    visited = [[False] * 5 for _ in range(5)]
                    visited[r][c] = True
                    while q:
                        curR, curC, cost, = q.popleft()
                        if 2 <= cost:
                            continue
                        for i in range(4):
                            movedR, movedC = curR + dR[i], curC + dC[i]
                            if not 0 <= movedR < 5 or not 0 <= movedC < 5:
                                continue
                            if visited[movedR][movedC] or place[movedR][movedC] == 'X':
                                continue
                            if place[movedR][movedC] == 'P':
                                flag = True
                                result[idx] = 0
                                break
                            visited[movedR][movedC] = True
                            q.append([movedR, movedC, cost + 1])

                        if flag:
                            break
                if flag:
                    break
            if flag:
                break
    return result

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
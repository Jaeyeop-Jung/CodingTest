
def getScore(r, c, targetR, targetC, img):
    blackCount = 0
    whiteCount = 0
    for i in range(r + 1, targetR):
        for j in range(c + 1, targetC):
            if img[i][j] == '#':
                blackCount += 1
            else:
                whiteCount += 1
    n = targetR - r + 1
    score = (blackCount / ((n - 2) ** 2)) * 100
    return score

def getSqaure(r, c, img):
    r1, c1, r2, c2 = r, c, r, c
    result = []
    while True:
        r1 += 1
        c2 += 1
        if len(img) <= r1 or len(img[r]) <= c2:
            break

        if img[r1][c1] == '#' and img[r2][c2] == '#':
            if r1 - r + 1 < 3:
                continue

            targetR, targetC = r1, c2
            testR1, testC1, testR2, testC2 = r1, c1, r2, c2
            while testR2 < targetR or testC1 < targetC:
                testR2 += 1
                testC1 += 1
                if img[testR1][testC1] != '#' or img[testR2][testC2] != '#':
                    break
            else:
                result.append(getScore(r, c, targetR, targetC, img))

        if img[r1][c1] == '.' or img[r2][c2] == '.':
            break
    return result


def solution(low, high, img):
    result = 0
    for r in range(len(img)):
        for c in range(len(img[r])):
            if img[r][c] == '#':
                sqaure = getSqaure(r, c, img)
                for i in range(len(sqaure)):
                    if low <= sqaure[i] < high:
                        result += 1
    return result


print(solution(25, 51, [".########......", ".####...#......", ".#.####.#.#####", ".#.#..#.#.#..##", ".#.##.#.#.#...#", ".#.####.#.#...#", ".#....###.#####", ".########......"]))





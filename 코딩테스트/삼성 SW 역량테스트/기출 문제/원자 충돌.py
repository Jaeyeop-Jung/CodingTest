'''
m개의 원자 [질량, 방향, 속력, 초기 위치]
방향은 대각선 포함
격자는 원형처럼 나가면 반대쪽으로 돌아옴
1. 자신의 방향으로 자신의 속력만큼 이동
2. 2개의 원자가 있는 칸은
    a. 질량과 속력을 모두 합한 원자 하나로 만듬
    b. 원자는 4개로 나누어짐
    c. 질량은 질량 / 5, 속도 = 속력 / cnt, 모두 같으면 상하좌우 아니면 대각선
    d. 소수점 버림
    e. 질량이 0이면 소멸
'''

dR = [-1, -1, 0, 1, 1, 1, 0, -1]
dC = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k, = map(int, input().split())
arr = [[[] for _ in range(n)] for _ in range(n)]
atom = {}
atomNumCnt = 0
for _ in range(m):
    r, c, m, s, d, = map(int, input().split())
    arr[r - 1][c - 1].append(atomNumCnt)
    atom[atomNumCnt] = [r - 1, c - 1, m, s, d]
    atomNumCnt += 1

def move():
    newArr = [[[] for _ in range(n)] for _ in range(n)]
    for atomNum in atom:
        r, c, m, s, d, = atom[atomNum]
        movedR, movedC = r + dR[d] * s, c + dC[d] * s
        movedR, movedC = movedR % n, movedC % n
        newArr[movedR][movedC].append(atomNum)
        atom[atomNum] = [movedR, movedC, m, s, d]
    return newArr

def combine():
    newArr = [[[] for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if 2 <= len(arr[r][c]):
                totalM, totalS, = 0, 0
                totalD = []
                for atomNum in arr[r][c]:
                    _, _, m, s, d = atom[atomNum]
                    totalM += m
                    totalS += s
                    totalD.append(d % 2)

                nextM, nextS = int(totalM / 5),  int(totalS / len(arr[r][c]))
                if len(set(totalD)) == 1:
                    nextD = [0, 2, 4, 6]
                else:
                    nextD = [1, 3, 5, 7]

                for atomNum in arr[r][c]:
                    del atom[atomNum]

                if nextM == 0:
                    continue

                for i in range(4):
                    global atomNumCnt
                    newArr[r][c].append(atomNumCnt)
                    atom[atomNumCnt] = [r, c, nextM, nextS, nextD[i]]
                    atomNumCnt += 1
            else:
                newArr[r][c] = arr[r][c]
    return newArr

for _ in range(k):
    arr = move()
    arr = combine()

result = 0
for atomNum in atom:
    result += atom[atomNum][2]
print(result)

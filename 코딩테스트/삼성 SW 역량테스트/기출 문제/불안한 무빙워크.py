'''
up, down 정의
1. 무빙 워크 회전
2. 무빙 워크 오른쪽부터 앞에 사람이 없거나 0이 아니면 이동
3. 1번칸에 사람이 없고, 안정성이 0이 아니면 사람 올림. 안정성 - 1됨.
'''

from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))
up = deque(arr[:n])
down = deque(arr[n:][::-1])
upPerson = deque(False for _ in range(n))

def checkArrive():
    if upPerson[-1]:
        upPerson[-1] = False

def isFinish():
    if k <= up.count(0) + down.count(0):
        return False
    return True

round = 0
while isFinish():

    round += 1

    # 1
    upPerson.rotate(1)
    down.append(up.pop())
    up.appendleft(down.popleft())
    checkArrive()

    # 2
    for i in range(n - 2, -1, -1):
        if upPerson[i] and not upPerson[i + 1] and 0 < up[i + 1]:
            upPerson[i + 1] = True
            up[i + 1] -= 1
            upPerson[i] = False
            checkArrive()

    # 3
    if not upPerson[0] and 0 < up[0]:
        upPerson[0] = True
        up[0] -= 1


print(round)
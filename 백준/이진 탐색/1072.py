import sys

input = sys.stdin.readline

x, y = map(int, input().split())

start = 1
end = sys.maxsize - x
winPer = int(y * 100 / x)
playRound = 0
while start <= end:
    mid = (start + end) // 2
    winPerTemp = int((y + mid) / (x + mid) * 100)
    if winPerTemp > winPer:
        playRound = mid
        end = mid - 1
    else:
        start = mid + 1

if playRound == 0 or winPer == 99:
    print(-1)
else:
    print(playRound)



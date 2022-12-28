import sys
input = sys.stdin.readline

mini, maxi = map(int, input().split())
arr = [True] * (maxi - mini + 1)
for i in range(2, maxi):
    cur = i ** 2
    if maxi < cur:
        break
    start = mini // cur
    while start * cur <= maxi:
        if not mini <= start * cur <= maxi:
            start += 1
            continue
        arr[start * cur - mini] = False
        start += 1

print(arr.count(True))
# 1000000000000 1000001000000
# 101 102 103 105 106 107 109 110
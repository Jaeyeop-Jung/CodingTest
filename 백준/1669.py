
def isAvailable(cur, added, end):
    rest = end - cur
    total = (added * (added + 1)) // 2
    return total <= rest

start, end = map(int, input().split())
res = 0
if end <= start:
    start, end = end, start

if start == end:
    print(0)
    exit()

added = 1
cur = start + 1
res = 1
while cur != end:
    if isAvailable(cur, added + 1, end):
        added += 1
        cur += added
    elif isAvailable(cur, added, end):
        cur += added
    else:
        added -= 1
        cur += added
    res += 1

print(res)
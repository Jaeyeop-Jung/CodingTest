from itertools import combinations

l, c = map(int, input().split())
arr = list(input().split())
arr.sort()

result = set()
for i in combinations(arr, l):
    temp = ''.join(sorted(list(i)))
    moemCount = 0
    for moem in ['a', 'e', 'i', 'o', 'u']:
        moemCount += temp.count(moem)
    if not 1 <= moemCount:
        continue
    if not 2 <= len(temp) - moemCount:
        continue

    result.add(temp)

for i in sorted(list(result)):
    print(i)
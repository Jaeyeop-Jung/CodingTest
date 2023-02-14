import math
from collections import Counter

t = int(input())
for _ in range(t):
    s = input()
    n = int(input())

    result3 = math.inf
    count = dict(Counter(s))
    for each in count:
        if n <= count[each]:
            indexes = [i for i in range(len(s)) if each == s[i]]
            for i in range(len(indexes) - n + 1):
                result3 = min(result3, indexes[i + n - 1] - indexes[i] + 1)
    if result3 == math.inf:
        print(-1)
        continue

    result4 = 0
    for each in count:
        if n <= count[each]:
            indexes = [i for i in range(len(s)) if each == s[i]]
            for i in range(len(indexes) - n + 1):
                result4 = max(result4, indexes[i + n - 1] - indexes[i] + 1)
    if result4 == 0:
        print(-1)
        continue

    print(f'{result3} {result4}')

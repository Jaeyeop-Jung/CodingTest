import sys
from itertools import combinations
from string import ascii_lowercase
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(input()[4:-4])
if k < 5:
    print(0)
    exit()

k -= 5
dic = {
    'a': 0,
    'n': 0,
    't': 0,
    'i': 0,
    'c': 0,
}
alphabet_list = list(ascii_lowercase)
for key in dic:
    alphabet_list.remove(key)

result = 0
for i in combinations(alphabet_list, k):
    temp = list(i)
    for j in temp:
        dic[j] = 0

    cnt = 0
    for j in arr:
        for k in j:
            if k not in dic:
                break
        else:
            cnt += 1

    for j in temp:
        del dic[j]

    result = max(result, cnt)
    if cnt == n:
        break

print(result)
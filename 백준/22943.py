
k, m = map(int, input().split())
maxi = ''
num = 9
for i in range(k):
    maxi += str(num)
    num -= 1

maxi = int(maxi)
a = [False, False] + [True] * (maxi - 1)
primes=[]
for i in range(2,maxi + 1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, maxi+1, i):
        a[j] = False

one = set()
two = set()
for i in range(len(primes)):
    for j in range(i, len(primes)):
        cur = primes[i] + primes[j]
        if cur <= maxi and i != j:
            one.add(cur)
        cur = primes[i] * primes[j]
        if cur <= maxi:
            two.add(cur)

res = 0
def dfs(cnt, cur, visited):
    if cnt == k:
        toInt = int(cur)
        while toInt % m == 0:
            toInt //= m
        if toInt in one and toInt in two:
            global res
            res += 1
        return

    for i in range(10):
        if (cnt == 0 and i == 0) or visited[i]:
            continue
        visited[i] = True
        dfs(cnt + 1, cur + str(i), visited)
        visited[i] = False


dfs(0, '', [False] * 10)
print(res)
import sys

input = sys.stdin.readline

n, m, = map(int, input().split())
arr = list(map(int, input().split()))

diff = [arr[i + 1] - arr[i] for i in range(n - 1)]
diff.sort()
for _ in range(m - 1):
    diff.pop()

print(sum(diff))
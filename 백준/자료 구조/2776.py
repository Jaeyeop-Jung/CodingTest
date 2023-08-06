import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    arr = set([i for i in nums])

    m = int(input())
    nums = list(map(int, input().split()))
    for num in nums:
        if num in arr:
            print('1')
        else:
            print('0')

import sys

input = sys.stdin.readline

n = int(input())

s = set()
for i in range(n):
    command = list(input().split())
    if 1 < len(command):
        command[1] = int(command[1])
    if command[0] == 'all':
        s = set(i for i in range(1, 21))
    elif command[0] == 'empty':
        s = set()
    elif command[0] == 'add':
        s.add(command[1])
    elif command[0] == 'remove':
        s.discard(command[1])
    elif command[0] == 'check':
        if command[1] in s:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        if command[1] in s:
            s.discard(command[1])
        else:
            s.add(command[1])

from collections import deque

s = input()
q = deque()
for i in range(len(s)):
    q.append(s[i])
    while 4 <= len(q):
        if q[-1] == 'P' and q[-2] == 'A' and q[-3] == 'P' and q[-4] == 'P':
            q.pop()
            q.pop()
            q.pop()
            q.pop()
            q.append('P')
        else:
            break

join = ''.join(q)
if join != 'P':
    print('NP')
else:
    print('PPAP')
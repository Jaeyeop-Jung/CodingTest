
s = input()
t = input()

while len(s) != len(t):
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1][::-1]

print(1 if s == t else 0)

s = input()
t = input()

def dfs(cur):
    if len(cur) <= len(s):
        if cur == s:
            print(1)
            exit()
        return

    if cur[-1] == 'A':
        dfs(cur[:-1])
    if cur[0] == 'B':
        dfs(cur[::-1][:-1])


dfs(t)
print(0)
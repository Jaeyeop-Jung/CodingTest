# TODO 틀림 이건 맞아야지.. 잘 생각해봐

s = input()
t = input()

def dfs(cur):
    if len(cur) == len(s):
        if cur == s:
            global result
            result = True
        return

    if cur[0] == 'B':
        dfs(cur[::-1][:len(cur) - 1])
    if cur[-1] == 'A':
        dfs(cur[:len(cur) - 1])


result = False
dfs(t)
print(1 if result else 0)
import math

n = int(input())
res = ''

def isPossible(string):
    temp = ''
    for i in range(len(string) - 1, -1, -1):
        temp += string[i]
        if len(temp) % 2 == 0:
            for sep in range(len(temp)):
                if temp[:sep] == temp[sep:]:
                    return False
    return True

def dfs(cur, string):
    if cur == n:
        # global res
        # res = min(res, int(string))
        print(string)
        exit()
        return

    for i in range(1, 4):
        if isPossible(string + str(i)):
            dfs(cur + 1, string + str(i))

res = math.inf
dfs(0, '')
print(res)
import math

result = math.inf

def isOneDiff(str1, str2):
    cnt = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            cnt += 1
    if 1 < cnt:
        return False
    return True

def dfs(words, visited, now, target, cnt):
    if now == target:
        global result
        result = min(result, cnt + 1)
        return
    visited[now] = True
    for i in range(len(words)):
        if visited[i] is False and isOneDiff(words[now], words[i]):
            dfs(words, visited, i, target, cnt + 1)
            visited[i] = False

def solution(begin, target, words):
    if target not in words:
        return 0

    for i in range(len(words)):
        if isOneDiff(begin, words[i]):
            dfs(words, [False] * len(words), i, words.index(target), 0)
    return result


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
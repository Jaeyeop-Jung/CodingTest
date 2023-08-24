# from itertools import permutations
#
# n = int(input())
# arr = [input() for _ in range(n)]
# first = set()
# s = set()
# for i in arr:
#     first.add(i[0])
#     for j in i:
#         s.add(j)
#
# s = sorted(list(s))
# res = 0
# cnt = 0
# for per in permutations([i for i in range(10)], len(s)):
#     if 0 in per and s[per.index(0)] in first:
#         continue
#
#     tempRes = 0
#     dic = {}
#     for i in range(len(s)):
#         dic[s[i]] = per[i]
#     for i in arr:
#         temp = ''
#         for j in i:
#             temp += str(dic[j])
#         tempRes += int(temp)
#     res = max(res, tempRes)
#
# print(res)

# n = int(input())
# dic = {i: {j: 0 for j in range(ord('A'), ord('K'))} for i in range(15)}
# arr = []
# alpha = set()
# for _ in range(n):
#     s = input()
#     arr.append(s)
#     for j in range(len(s) - 1, -1, -1):
#         dic[14 - j][ord(s[j])] += 1
#         alpha.add(s[j])
#
# res = 0
# def dfs(cur, idx, match):
#     if idx == 15:
#         global res
#         temp = 0
#         for i in arr:
#             change = i
#             for string in match:
#                 change = change.replace(chr(string), str(match[string]))
#             temp += int(change)
#         res = max(res, temp)
#         return
#
#     temp = [[key, dic[idx][key]] for key in dic[idx]]
#     temp.sort(key=lambda x: -x[1])
#     if sum([i[1] for i in temp]) == 0:
#         dfs(cur, idx + 1, match)
#     else:
#         for key, value in temp:
#             if key in match or chr(key) not in alpha:
#                 continue
#             match[key] = cur
#             dfs(cur - 1, idx + 1, match)
#             del match[key]
#
#
# dfs(9, 0, {})
# print(res)

n = int(input())
dic = {i: 0 for i in range(ord('A'), ord('J') + 1)}
arr = []
first = set()
for i in range(n):
    s = input()
    arr.append(s)
    score = 1
    first.add(s[0])
    for j in range(len(s) - 1, -1, -1):
        dic[ord(s[j])] += score
        score *= 10

change = {}
temp = [[key, dic[key]] for key in dic]
temp.sort(key=lambda x: x[1])
# 0 먼저 넣고
for i in range(len(temp)):
    if chr(temp[i][0]) not in first:
        change[chr(temp[i][0])] = str(0)
        temp.pop(i)
        break

# 나머지
temp.sort(key=lambda x: -x[1])
cnt = 9
for key, value in temp:
    change[chr(key)] = str(cnt)
    cnt -= 1

res = 0
for i in arr:
    for key in change:
        i = i.replace(key, change[key])
    res += int(i)
print(res)
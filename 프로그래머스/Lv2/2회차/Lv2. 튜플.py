import re
from collections import Counter

# def solution(s):
#     result = []
#     s = s[1:-1]
#     s = s.split('},')
#     s[-1] = s[-1][:-1]
#     for i in range(len(s)):
#         s[i] = s[i][1:]
#     s.sort(key=lambda x:len(x))
#     for i in s:
#         arr = i.split(',')
#         for j in arr:
#             if int(j) not in result:
#                 result.append(int(j))
#     return result

def solution(s):
    result = []
    for i in re.findall('[\d]', s):
        if int(i) not in result:
            result.append(int(i))
    return result

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
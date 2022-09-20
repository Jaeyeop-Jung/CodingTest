#
# def solution(word):
#     dic = ['', 'A', 'E', 'I', 'O', 'U']
#     result = 0
#     for i in range(1, len(dic)):
#         for j in range(len(dic)):
#             for k in range(len(dic)):
#                 for a in range(len(dic)):
#                     for b in range(len(dic)):
#                         if j == 0 and (k != 0 or a != 0 or b != 0):
#                             continue
#                         elif k == 0 and (a != 0 or b != 0):
#                             continue
#                         elif a == 0 and (b != 0):
#                             continue
#                         result += 1
#                         if word == dic[i] + dic[j] + dic[k] + dic[a] + dic[b]:
#                             return result
#                         print(dic[i] + dic[j] + dic[k] + dic[a] + dic[b])

from itertools import product

def solution(word):
    print(sorted([''.join(c) for i in range(5) for c in product("AEIOU",  repeat=i+1)]))


# print(solution('AAAAE'))
# print(solution('AAAE'))
# print(solution('I'))
# print(solution('AUUUU'))
print(solution('EIO'))
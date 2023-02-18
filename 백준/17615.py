# TODO 잘 생각해봐 최적화를 더 해보면 될듯

n = int(input())
s = input()

# RCnt = 0
# for i in range(len(s) - 1, -1, -1):
#     if s[i] == 'B':
#         RCnt += s[:i].count('R')
#         break
#
# BCnt = 0
# turn = False
# for i in range(len(s) - 1, -1, -1):
#     if s[i] == 'R':
#         # turn = True
#         BCnt += s[:i].count('B')
#         break
#     # if s[i] == 'B' and turn:
#     #     # turn = False
#     #     BCnt += 1
#
# print(min(RCnt, BCnt))

red = s.count('R')
blue = n - red
ans = min(red, blue)

cnt = 0
for i in range(len(s)):
    if s[i] != s[0]:
        break
    cnt += 1
if s[0] == 'R':
    ans = min(ans, red - cnt)
else:
    ans = min(ans, blue - cnt)
# TODO 틀림

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
con = [[0]+[-1e9]*m for i in range(n+1)]
notcon = [[0]+[-1e9]*m for i in range(n+1)]

for i in range(1, n+1):
    num = int(input())
    for j in range(1, min(m, (i+1)//2)+1):
        notcon[i][j]=max(con[i-1][j], notcon[i-1][j])
        con[i][j]=max(con[i-1][j], notcon[i-1][j-1])+num
print(max(con[n][m], notcon[n][m]))
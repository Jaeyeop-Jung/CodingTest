
n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

for i in range(k):
    B.sort()
    if A[i] < B[len(B) - 1]:
        A[i], B[len(B) - 1] = B[len(B) - 1], A[i]

print(sum(A))
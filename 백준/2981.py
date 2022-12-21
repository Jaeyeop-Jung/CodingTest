# TODO 틀림 수학적 접근이 필요하다.
# https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-2981-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B2%80%EB%AC%B8-%EA%B3%A8%EB%93%9C5-%EC%A0%95%EC%88%98%EB%A1%A0

import math

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

r_list = [arr[1] - arr[0]]
for i in range(1, len(arr) - 1):
    r_list.append(arr[i + 1] - arr[i])

gcd = r_list[0]
for i in range(1, len(r_list)):
    gcd = math.gcd(gcd, r_list[i])

result = set()
for i in range(2, int(gcd ** 0.5) + 1):
    if gcd % i == 0:
        result.add(i)
        result.add(gcd // i)
result.add(gcd)
print(*sorted(list(result)))
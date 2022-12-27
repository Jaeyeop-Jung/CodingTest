# TODO 틀림

n = int(input())

if n == 1:
    print(0)
    exit()
elif n == 2:
    print(1)
    exit()

isPrime = [True] * (n + 1)
prime = []
for i in range(2, len(isPrime)):
    if isPrime[i]:
        prime.append(i)
        j = 1
        while i * j < len(isPrime):
            isPrime[i * j] = False
            j += 1

left, right = 0, 0
temp = prime[0]
result = 0
while left < len(prime) and right < len(prime):
    if temp == n:
        result += 1
        temp -= prime[left]
        left += 1
        continue
    if temp < n:
        right += 1
        if len(prime) <= right:
            break
        temp += prime[right]
    else:
        temp -= prime[left]
        left += 1

print(result)


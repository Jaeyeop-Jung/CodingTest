import math

def lcm(a, b):
    return a * b / math.gcd(a, b)

e, s, m, = map(int, input().split())
result = 1
eTemp, sTemp, mTemp = 1, 1, 1
while True:
    if e == eTemp and s == sTemp and m == mTemp:
        break
    eTemp += 1
    eTemp %= 16
    if eTemp == 0:
        eTemp += 1
    sTemp += 1
    sTemp %= 29
    if sTemp == 0:
        sTemp += 1
    mTemp += 1
    mTemp %= 20
    if mTemp == 0:
        mTemp += 1
    result += 1

print(result)


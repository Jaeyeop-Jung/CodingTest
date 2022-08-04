
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


a = 15
b = 3
print(gcd(a, b))
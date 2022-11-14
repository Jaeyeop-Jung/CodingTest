import math

def solution(arrayA, arrayB):
    aGCD = arrayA[0]
    bGCD = arrayB[0]
    for i in range(1, len(arrayA)):
        aGCD = math.gcd(aGCD, arrayA[i])
        bGCD = math.gcd(bGCD, arrayB[i])

    aGCDs = []
    bGCDs = []
    for i in range(aGCD, 0, -1):
        if aGCD % i == 0:
            aGCDs.append(i)
    for i in range(bGCD, 0, -1):
        if bGCD % i == 0:
            bGCDs.append(i)

    amax = 0
    bmax = 0
    for i in aGCDs:
        for j in arrayB:
            if j % i == 0:
                break
        else:
            amax = i
            break
    for i in bGCDs:
        for j in arrayA:
            if j % i == 0:
                break
        else:
            bmax = i
            break
    return max(amax, bmax)



print(solution([10, 17], [5, 20]))
print(solution([10, 20], [5, 17]))
print(solution([14, 35, 119], [18, 30, 102]))
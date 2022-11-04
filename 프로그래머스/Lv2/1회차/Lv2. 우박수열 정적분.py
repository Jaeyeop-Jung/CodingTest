
def getUbak(k):
    ubak = [[0, k]]
    cnt = 1
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        ubak.append([cnt, k])
        cnt += 1
    return ubak

def solution(k, ranges):
    ubak = getUbak(k)
    neobi = [(ubak[i][1] + ubak[i + 1][1]) / 2 for i in range(len(ubak) - 1)]
    # neobi = [sum(neobi[:i + 1]) for i in range(len(neobi))]

    result = []
    for i, j in ranges:
        if len(ubak) - 1 + j < i:
            result.append(-1.0)
        elif len(ubak) - 1 + j == i - 1:
            result.append(sum(neobi))
        else:
            result.append(sum(neobi[i:len(ubak) - 1 + j]))

    return result

print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]]))

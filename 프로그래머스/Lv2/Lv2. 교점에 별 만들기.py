from pprint import pprint


def solution(line):
    coord = set()
    for i in range(len(line)):
        for j in range(len(line)):
            if i != j:
                a, b, e = line[i]
                c, d, f = line[j]
                if (a * d - b * c) == 0 or (a * d - b * c) == 0:
                    continue
                x = (b * f - e * d) / (a * d - b * c)
                y = (e * c - a * f) / (a * d - b * c)
                if x.is_integer() and y.is_integer():
                    coord.add((int(x), int(y)))

    xMin, xMax = min([i[0] for i in coord]), max([i[0] for i in coord])
    yMin, yMax = min([i[1] for i in coord]), max([i[1] for i in coord])
    result = ['.' * (xMax - xMin + 1)] * (yMax - yMin +1)
    for x, y in coord:
        result[yMax - y] = result[yMax - y][:x - xMin] + '*' + result[yMax -y][x - xMin + 1:]
        # print(yMax - y, xMax - x)
    # pprint(result)
    return result



print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))

def solution(s):
    input = list(map(int, s.split(' ')))
    return str(min(input)) + " " + str(max(input))

print(solution("-1 -2 -3 -4"))
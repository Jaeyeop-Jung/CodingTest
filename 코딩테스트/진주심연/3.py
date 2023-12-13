from itertools import combinations

def solution(phone_number, birthday):
    no = set()
    phone_number = phone_number[5:]
    p = list(phone_number)
    b = list(birthday)

    for i in combinations(p, 4):
        no.add(''.join(i))

    for i in combinations(b, 4):
        no.add(''.join(i))

    res = 0
    for i in range(10000):
        cur = str(i).rjust(4, '0')
        if cur in no:
            continue
        for num in range(10):
            if 3 <= cur.count(str(num)):
                break
        else:
            res += 1
    return res


print(solution('(010)54662345', '20010923'))
print(solution('(010)11111111', '20020111'))
print(solution('(010)12345678', '19990909'))
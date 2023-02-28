# TODO 틀림 잘 생각해봐 이건 맞아야된다 맞을 수 있음

def update(parent):
    for i in range(50 * 50):
        find_parent(parent, i)

def toTwo(integer):
    return integer // 50, integer % 50

def toOne(r, c):
    return r * 50 + c

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(commands):
    arr = [[''] * 50 for _ in range(50)]
    result = []
    parent = [i for i in range(50 * 50)]
    for command in commands:
        length = len(command.split(' '))
        if command.startswith('UPDATE') and length == 4:
            com, r, c, v, = command.split(' ')
            r, c = int(r) - 1, int(c) - 1
            p = find_parent(parent, toOne(r, c))
            r, c, = toTwo(p)
            arr[r][c] = v
        elif command.startswith('UPDATE') and length == 3:
            com, v1, v2 = command.split(' ')
            for r in range(50):
                for c in range(50):
                    if arr[r][c] == v1:
                        arr[r][c] = v2
        elif command.startswith('MERGE'):
            com, r1, c1, r2, c2 = command.split(' ')
            r1, c1, r2, c2 = int(r1) - 1, int(c1) - 1, int(r2) - 1, int(c2) - 1
            if find_parent(parent, toOne(r1, c1)) == find_parent(parent, toOne(r2, c2)):
                continue
            p1 = find_parent(parent, toOne(r1, c1))
            p1R, p1C = toTwo(p1)
            p2 = find_parent(parent, toOne(r2, c2))
            p2R, p2C = toTwo(p2)
            if arr[p1R][p1C] == '' or arr[p2R][p2C] == '':
                changed = arr[p1R][p1C] if arr[p1R][p1C] else arr[p2R][p2C]
                union_parent(parent, p1, p2)
                pR, pC = toTwo(find_parent(parent, p1))
                arr[pR][pC] = changed
            else:
                pR, pC, = toTwo(find_parent(parent, toOne(r1, c1)))
                changed = arr[pR][pC]
                union_parent(parent, toOne(r1, c1), toOne(r2, c2))
                pR, pC, = toTwo(find_parent(parent, toOne(r1, c1)))
                arr[pR][pC] = changed
        elif command.startswith('UNMERGE'):
            com, r, c = command.split(' ')
            r, c = int(r) - 1, int(c) - 1
            pR, pC, = toTwo(find_parent(parent, toOne(r, c)))
            changed = arr[pR][pC]
            update(parent)
            change = []
            for i in range(50 * 50):
                if find_parent(parent, i) == find_parent(parent, toOne(r, c)):
                    change.append(i)
            for i in change:
                cR, cC, = toTwo(i)
                arr[cR][cC] = ''
                parent[i] = i
            arr[r][c] = changed
        elif command.startswith('PRINT'):
            com, r, c = command.split(' ')
            r, c = int(r) - 1, int(c) - 1
            r, c = toTwo(find_parent(parent, toOne(r, c)))
            result.append(arr[r][c] if arr[r][c] != '' else 'EMPTY')
    return result

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))
print(solution(['PRINT 1 1', 'UPDATE 1 1 A', 'PRINT 1 1']))
print(solution(["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 1 1 4 4", "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]))
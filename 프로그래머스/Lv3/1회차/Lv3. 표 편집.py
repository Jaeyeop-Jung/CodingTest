# TODO 틀림 구현 좀 더 깊이 생각해라

class Node:
    prev = None
    next = None
    removed = False

def up(dic, k):
    cnt = 0
    while cnt < 1:
        if dic[k].prev == None:
            break
        k = dic[k].prev
        if dic[k].removed is False:
            cnt += 1
    return k

def down(dic, k):
    cnt = 0
    while cnt < 1:
        if dic[k].next == None:
            break
        k = dic[k].next
        if dic[k].removed is False:
            cnt += 1
    return k

def solution(n, k, cmd):
    dic = {}
    trash = []
    for i in range(n):
        dic[i] = Node()
        if i == 0:
            dic[i].next = i + 1
        elif i == n - 1:
            dic[i].prev = i - 1
        else:
            dic[i].prev = i - 1
            dic[i].next = i + 1


    for i in cmd:
        if i[0].startswith('U'):
            move = int(i[2:])
            for _ in range(move):
                k = dic[k].prev
        elif i[0].startswith('D'):
            move = int(i[2:])
            for _ in range(move):
                k = dic[k].next
        elif i[0].startswith('C'):
            dic[k].removed = True
            trash.append(k)
            prev, next = dic[k].prev, dic[k].next
            if prev is not None:
                dic[prev].next = next
            if next is not None:
                dic[next].prev = prev
            if dic[k].next is None:
                k = dic[k].prev
            else:
                k = dic[k].next
        else:
            pop = trash.pop()
            dic[pop].removed = False
            if dic[pop].prev == None:
                temp = down(dic, pop)
                dic[pop].next = temp
                dic[temp].prev = pop
            elif dic[pop].next == None:
                temp = up(dic, pop)
                dic[pop].prev = temp
                dic[temp].next = pop
            else:
                upTemp = up(dic, pop)
                downTemp = down(dic, pop)
                dic[upTemp].next = pop
                dic[downTemp].prev = pop

    result = ''
    for i in range(n):
        if dic[i].removed is True:
            result += 'X'
        else:
            result += 'O'
    return result

print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
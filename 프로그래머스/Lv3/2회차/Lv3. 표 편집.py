# TODO 틀림 다 풀어놓고 실수함;; 다시 할 땐 맞아야지

class Node:
    def __init__(self, previous, next):
        self.previous = previous
        self.next = next
        self.removed = False

def solution(n, k, cmd):
    arr = [Node(None, None) for i in range(n)]
    arr[0].next = arr[1]
    for i in range(1, n - 1):
        arr[i].previous = arr[i-1]
        arr[i].next = arr[i+1]
    arr[-1].previous = arr[-2]

    removed = []
    cur = arr[k]
    for command in cmd:
        if command[0] == 'U':
            for i in range(int(command[2:])):
                cur = cur.previous

        elif command[0] == 'D':
            for i in range(int(command[2:])):
                cur = cur.next

        elif command[0] == 'C':
            if cur.previous != None:
                cur.previous.next = cur.next
            if cur.next != None:
                cur.next.previous = cur.previous
            cur.removed = True
            removed.append(cur)
            if cur.next == None:
                cur = cur.previous
            else:
                cur = cur.next

        else:
            pop = removed.pop()
            if pop.previous != None:
                pop.previous.next = pop
            if pop.next != None:
                pop.next.previous = pop
            pop.removed = False

    result = ''
    for i in arr:
        if i.removed == True:
            result += 'X'
        else:
            result += 'O'
    return result

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
# print(solution(4, 0, ["D 5", "C", "Z", "C", "Z", "U 1", 'C', 'U 2', 'C', 'C', 'C', 'C']))
# TODO 틀림 이건 맞아야지;;

# cur = input()
# n = int(input())
# cursor = len(cur)
# for _ in range(n):
#     command = input()
#     if command.startswith('L'):
#         cursor -= 1 if 0 <= cursor - 1 else cursor
#     elif command.startswith('D'):
#         cursor += 1 if cursor + 1 <= len(cur) else cursor
#     elif command.startswith('B'):
#         if cursor == 0:
#             continue
#         cur = cur[:cursor - 1] + cur[cursor:]
#         cursor -= 1
#     else:
#         c, t = command.split(' ')
#         cur = cur[:cursor] + t + cur[cursor:]
#         cursor += 1
#
# print(cur)

class node:
    def __init__(self, prev, next, key):
        self.prev = prev
        self.next = next
        self.key = key


init = input()
n = int(input())
cur = node(None, None, init[0])
for i in range(1, len(init)):
    new = node(None, None, init[i])
    new.prev = cur
    cur.next = new
    cur = new

for _ in range(n):
    command = input()
    if command.startswith('L'):
        cur = cur.prev if cur.prev is not None else cur
    elif command.startswith('D'):
        cur = cur.next if cur.next is not None else cur
    elif command.startswith('B'):
        if cur is None:
            continue
        if cur.prev is None and cur.next is None:
            cur = None
        elif cur.prev is None:
            cur.next.prev = None
            cur = cur.next
        elif cur.next is None:
            cur.prev.next = None
            cur = cur.prev
    else:
        c, k = command.split(' ')
        if cur is None:
            cur = node(None, None, k)
        else:
            new = node(cur, None, k)
            if cur.next is not None:
                new.next = cur.next
                cur.next.prev = new
            cur.next = new
            cur = new

while cur.prev is not None:
    cur = cur.prev
result = ''
while cur is not None:
    result += cur.key
    cur = cur.next
print(result)
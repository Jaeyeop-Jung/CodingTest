
n = int(input())
pattern = input()
for _ in range(n):
    target = input()
    for i in range(len(pattern)):
        if pattern[i] == '*':
            rest = len(pattern) - i - 1
            if len(target) - i < rest:
                print('NE')
            elif pattern[i + 1:] == target[-rest:]:
                print('DA')
            else:
                print('NE')
            break
        elif pattern[i] != target[i]:
            print('NE')
            break

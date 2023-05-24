# TODO 틀림

string = input()

for i in range(len(string) - 1, 0, -1):
    dic = {}
    for start in range(len(string) + 1 - i):
        temp = string[start:start + i]
        if temp in dic:
            print(len(temp))
            exit()
        else:
            dic[temp] = 1
print(0)
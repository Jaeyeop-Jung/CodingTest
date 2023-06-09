# import re
#
# n = int(input())
# for _ in range(n):
#     string = input()
#     match = re.fullmatch('(100+1+|01)+', string)
#     if match == None:
#         print('NO')
#     else:
#         print('YES')

n = int(input())
for _ in range(n):
    string = input()
    index = 0
    while True:
        if len(string) <= index:
            print('YES')
            break
        if string[index] == '0':
            if index + 1 < len(string) and string[index + 1] == '1':
                index += 2
            else:
                print('NO')
                break
        else:
            if index + 3 < len(string):
                if string[index + 1] == '0' and string[index + 2] == '0':
                    index += 2
                    while index < len(string) and string[index] == '0':
                        index += 1
                    if len(string) <= index or string[index] != '1':
                        print('NO')
                        break
                    index += 1
                    while index < len(string) and string[index] == '1':
                        if string[index:index+3] == '100':
                            break
                        else:
                            index += 1
                else:
                    print('NO')
                    break
            else:
                print('NO')
                break